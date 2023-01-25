const puppeteer = require("puppeteer");
(async () => {
  const browser = await puppeteer.launch({ headless: false });

  const page = await browser.newPage();

  await page.goto("https://forms.gle/ssJqxQ81rSkQRPwu5");

  const element = await page.waitForSelector('[aria-labelledby="i1"]');

  // await page.type('[aria-labelledby="i1"]', "547554000");

  await page.waitForTimeout(50000);

  await browser.close();
})();
