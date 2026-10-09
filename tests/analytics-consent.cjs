/* Browser integration tests. All external requests are intercepted.
   The Google library is replaced with a test double: live GA verification is separate.
   Run after a Hugo build:
   ANALYTICS_BUILD_DIR=/tmp/hotmanoglu-analytics-build PLAYWRIGHT_MODULE=/path/to/playwright node tests/analytics-consent.cjs */
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const build = process.env.ANALYTICS_BUILD_DIR || path.resolve('public');
const site = 'https://www.hotmanoglu.com';
const article = '/posts/680-sahte-insan-torontonun-sentetik-kimlik-fabrikasi-nasil-calisiyordu/';
const key = 'hm-analytics-consent-v1';
const google = /(^|\.)(google\.com|googletagmanager\.com|google-analytics\.com|googleapis\.com|gstatic\.com|doubleclick\.net)$/;
const mime = {'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.woff2':'font/woff2','.svg':'image/svg+xml','.png':'image/png','.webp':'image/webp','.jpg':'image/jpeg'};
const mock = `(() => {
  const events = window.dataLayer || []; let cursor = 0;
  function consume() {
    while (cursor < events.length) {
      const args = events[cursor++];
      if (args[0] === 'config') {
        document.cookie = '_ga=synthetic-client; Path=/; Domain=www.hotmanoglu.com; SameSite=Lax; Secure';
        document.cookie = '_ga_KKHBRTL8LJ=synthetic-session; Path=/; Domain=www.hotmanoglu.com; SameSite=Lax; Secure';
      }
      if (args[0] === 'event' && !window['ga-disable-G-KKHBRTL8LJ']) {
        fetch('https://www.google-analytics.com/g/collect', {method:'POST', body:JSON.stringify({name:args[1], fields:args[2]})});
      }
    }
  }
  const push = events.push.bind(events);
  events.push = (...args) => { const result = push(...args); consume(); return result; };
  consume();
})();`;
async function run() {
 const browser = await chromium.launch({headless:true, executablePath:process.env.CHROME_EXECUTABLE || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const summaries = [];
 async function fixture(options={}) {
  const context = await browser.newContext({viewport:options.mobile ? {width:390,height:844} : {width:1440,height:1000}});
  const requests=[], payloads=[], errors=[];
  await context.route('**/*', async route => {
   const request=route.request(), url=new URL(request.url());
   if (google.test(url.hostname)) requests.push(request.url());
   if (url.hostname === 'www.googletagmanager.com') return route.fulfill({contentType:'text/javascript',body:mock});
   if (url.hostname === 'www.google-analytics.com') {payloads.push(JSON.parse(request.postData()));return route.fulfill({status:204});}
   if (!['www.hotmanoglu.com','ofis.hotmanoglu.com'].includes(url.hostname)) return route.abort();
   let filename = decodeURIComponent(url.pathname);
   if (filename.endsWith('/')) filename += 'index.html';
   if (options.page404 && request.resourceType() === 'document') filename='/404.html';
   try { const body=await fs.readFile(path.join(build, filename)); await route.fulfill({contentType:mime[path.extname(filename)] || 'application/octet-stream',body}); }
   catch { await route.fulfill({status:404,body:'Not found'}); }
  });
  const page=await context.newPage();
  page.on('pageerror', e=>errors.push(e.message));
  if (options.saved) await context.addInitScript(({key,choice,at})=>{if (!localStorage.getItem(key)) localStorage.setItem(key,JSON.stringify({choice,at}));},{key,choice:options.saved,at:options.expired ? Date.now()-181*86400000 : Date.now()});
  if (options.noStorage) await context.addInitScript(()=>{Storage.prototype.getItem=()=>{throw new Error('Storage blocked')};Storage.prototype.setItem=()=>{throw new Error('Storage blocked')};});
  await page.goto((options.host || site)+(options.path || article),{referer:options.referrer || 'https://www.google.com/search?q=private-search&email=synthetic@example.com',waitUntil:'networkidle'});
  return {context,page,requests,payloads,errors};
 }
 async function finish(f,label) {assert.deepEqual(f.errors,[]);summaries.push(label);await f.context.close();}
 const denied=await fixture();
 await denied.page.locator('#analyticsConsent').waitFor({state:'visible'});
 assert.equal(denied.requests.length,0);assert.equal((await denied.context.cookies()).filter(c=>c.name.startsWith('_ga')).length,0);
 await denied.page.locator('[data-analytics-choice="denied"]').click();
 await denied.page.reload({waitUntil:'networkidle'});
 assert.equal(denied.requests.length,0);assert.equal(denied.payloads.length,0);
 assert.equal(await denied.page.locator('#analyticsConsent').isVisible(),false);
 await finish(denied,'Initial visit and persisted rejection: zero Google requests / GA cookies');

 const accepted=await fixture({path:article+'?email=synthetic@example.com&token=dummy-sensitive&gclid=dummy-click&foo=secret&search=private-search&utm_source=linkedin&utm_medium=social&utm_campaign=article&utm_term=private-search&utm_content=synthetic@example.com#dummy-sensitive'});
 await accepted.page.locator('[data-analytics-choice="granted"]').click();
 await accepted.page.waitForFunction(()=>document.cookie.includes('_ga='));
 await accepted.page.waitForTimeout(100);
 assert.equal(accepted.requests.filter(u=>u.includes('/gtag/js')).length,1);
 assert.equal(accepted.payloads.filter(e=>e.name==='page_view').length,1);
 assert.equal(accepted.page.url(),site+article);
 const commands=await accepted.page.evaluate(()=>window.dataLayer.map(a=>Array.from(a)));
 const config=commands.find(a=>a[0]==='config')[2];
 assert.equal(config.send_page_view,false);assert.equal(config.cookie_domain,'www.hotmanoglu.com');assert.equal(config.cookie_expires,15552000);assert.equal(config.cookie_update,false);
 assert.equal(config.campaign_source,'linkedin');assert.equal(config.campaign_medium,'social');assert.equal(config.campaign_name,'article');
 assert.equal(config.allow_google_signals,false);assert.equal(config.allow_ad_personalization_signals,false);
 const consent=commands.find(a=>a[0]==='consent' && a[1]==='update')[2];
 for (const p of ['ad_storage','ad_user_data','ad_personalization']) assert.equal(consent[p],'denied');
 const serialized=JSON.stringify(commands);
 for (const marker of ['synthetic@example.com','dummy-sensitive','dummy-click','private-search','?email','utm_term','utm_content']) assert.equal(serialized.includes(marker),false,marker);
 assert.equal(config.page_referrer,'https://www.google.com/');
 await accepted.page.locator('[data-analytics-preferences]').click();
 await accepted.page.locator('[data-analytics-choice="granted"]').click();
 assert.equal(accepted.payloads.filter(e=>e.name==='page_view').length,1);
 await accepted.page.evaluate(()=>{document.querySelectorAll('a').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));});
 await accepted.page.locator('[data-copy-link]').click();
 await accepted.page.locator('a[href*="sharing/share-offsite"]').click();
 await accepted.page.evaluate(()=>{const a=document.createElement('a');a.id='syntheticOutbound';a.href='https://synthetic-token.example.com/path?email=synthetic@example.com#dummy-sensitive';a.textContent='synthetic@example.com';a.onclick=e=>e.preventDefault();document.body.appendChild(a);});
 await accepted.page.locator('#syntheticOutbound').click();
 await accepted.page.evaluate(()=>window.scrollTo(0,document.documentElement.scrollHeight));
 await accepted.page.waitForTimeout(150);
 await accepted.page.evaluate(()=>window.dispatchEvent(new Event('scroll')));
 await accepted.page.waitForTimeout(100);
 assert.equal(accepted.payloads.filter(e=>e.name==='scroll').length,1);
 assert(accepted.payloads.some(e=>e.name==='site_cta' && e.fields.cta_name==='copy_link'));
 assert(accepted.payloads.some(e=>e.name==='outbound_click' && e.fields.destination_type==='external'));
 assert(accepted.payloads.some(e=>e.name==='site_cta' && e.fields.cta_name==='share_linkedin'));
 assert.equal(JSON.stringify(accepted.payloads).includes('synthetic@example.com'),false);
 assert.equal(JSON.stringify(accepted.payloads).includes('synthetic-token'),false);
 const count=accepted.payloads.length;
 await accepted.page.locator('[data-analytics-preferences]').click();
 await Promise.all([accepted.page.waitForEvent('load'),accepted.page.locator('[data-analytics-choice="denied"]').click()]);
 await accepted.page.waitForLoadState('networkidle');
 assert.equal(accepted.payloads.length,count);assert.equal(await accepted.page.locator('script[src*="googletagmanager"]').count(),0);
 assert.equal((await accepted.context.cookies()).filter(c=>c.name.startsWith('_ga')).length,0);
 await finish(accepted,'Grant once, safe campaign/referrer/payload, scroll/CTA/outbound and revoke reload/cookie deletion');

 const returning=await fixture({saved:'granted',referrer:'https://synthetic-token.example.com/private?email=synthetic@example.com'});
 assert.equal(returning.payloads.filter(e=>e.name==='page_view').length,1);
 assert.equal(returning.payloads[0].fields.page_referrer,'');
 const second=await returning.context.newPage();await second.goto(site+'/',{waitUntil:'networkidle'});
 await second.locator('[data-analytics-preferences]').click();
 await Promise.all([returning.page.waitForEvent('load'),second.waitForEvent('load'),second.locator('[data-analytics-choice="denied"]').click()]);
 await returning.page.waitForLoadState('networkidle');await second.waitForLoadState('networkidle');
 assert.equal(await returning.page.locator('script[src*="googletagmanager"]').count(),0);
 assert.equal((await returning.context.cookies()).filter(c=>c.name.startsWith('_ga')).length,0);
 await finish(returning,'Returning grant / unknown referrer omitted / cross-tab revocation stops measurement');

 for (const options of [{expired:true,saved:'granted'},{host:'https://ofis.hotmanoglu.com'},{page404:true,path:'/unknown/'},{noStorage:true}]) {
  const f=await fixture(options);assert.equal(f.requests.length,0);assert.equal(f.payloads.length,0);
  if (options.expired || options.noStorage) assert.equal(await f.page.locator('#analyticsConsent').isVisible(),true);
  await finish(f,JSON.stringify(options)+': safe default, no Google request');
 }
 const mobile=await fixture({mobile:true});
 await mobile.page.screenshot({path:'/tmp/hotmanoglu-analytics-mobile.png',fullPage:false});
 const bounds=await mobile.page.locator('#analyticsConsent').boundingBox();assert(bounds.width <= 390 && bounds.x >= 0);assert(bounds.y >= 0 && bounds.y+bounds.height <= 844);
 await mobile.page.locator('[data-analytics-choice="denied"]').click();await finish(mobile,'Mobile banner fits viewport; rejection usable');
 console.log(JSON.stringify({passed:summaries.length,tests:summaries,liveGoogleLibrary:false},null,2));
 await browser.close();
}
run().catch(e=>{console.error(e);process.exit(1);});
