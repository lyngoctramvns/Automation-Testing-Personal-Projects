import { Locator, Page } from "@playwright/test";
import { MainPageComponents } from "../../components/storefront/MainPageComponents";

export default class BasePage {
  readonly page: Page;
  readonly submitButton: Locator;
  public mainPageComponents: MainPageComponents;

  constructor(page: Page) {
    this.page = page;
    this.submitButton = this.page.locator(
      `xpath=//button[@id="submitContact"]`
    );
    this.mainPageComponents = new MainPageComponents(this.page);
  }

  async clearBrowserCookies(context: any): Promise<any> {
    const page = await context.clearCookies();
    return page;
  }

  async clickStartBanner(): Promise<void> {
    const locateBanner = await this.mainPageComponents.getBannerButton()
    await locateBanner.click();
  }
}
