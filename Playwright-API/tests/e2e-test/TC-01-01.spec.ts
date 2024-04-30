import { chromium, Browser } from "@playwright/test";
import { test, expect, Page } from "@playwright/test";
import BasePage from "../../pages/base/BasePage";
import { BookingPage } from "../../pages/BookingPage";
import { MainPageComponents } from "../../components/storefront/MainPageComponents";

test.describe("The banner appear", async () => {
  test("Check the display of start banner", async () => {
    const browser: Browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page: Page = await context.newPage();
    const basePage: BasePage = new BasePage(page);
    const bookingPage: BookingPage = new BookingPage(page);
    const mainPageComponents: MainPageComponents = new MainPageComponents(page);

    await testScenario(basePage, bookingPage, mainPageComponents, context);
    await browser.close();
  });
});

// remember to alway have await before test.step

async function testScenario(
  basePage: BasePage,
  bookingPage: BookingPage,
  mainPageComponents: MainPageComponents,
  context: any
): Promise<void> {
  await test.step("Clear cookies from page and verify that the start banner exist", async () => {
    await bookingPage.visitMainPage();
    await basePage.clearBrowserCookies(context);
    const startBannerLocation = await mainPageComponents.getBannerButton();
    expect(startBannerLocation).toBeVisible();
  });
  await test.step("Click banner button and check if the banner disappeared", async () => {
    await bookingPage.visitMainPage();
    await basePage.clickStartBanner();
  });
}
