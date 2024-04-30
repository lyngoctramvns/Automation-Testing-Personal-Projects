import { Locator, Page } from "@playwright/test";

export class MainPageComponents {
  readonly page: Page;
  public bannerButton: Locator;

  constructor(page: Page) {
    this.page = page;
  }

  async getBannerButton(): Promise<Locator> {
    this.bannerButton = await this.page.locator(
      `xpath=//button[@class="btn btn-primary"]`
    );
    return this.bannerButton;
  }
}
