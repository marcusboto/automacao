import puppeteer from "puppeteer";

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto("https://forms.gle/ssJqxQ81rSkQRPwu5");
  // Fill field "Loja"
  await page.$eval("[aria-labelledby='i1']", (el) => (el.value = "547554000"));

  await page.waitForTimeout(50000);
  await browser.close();
})();
