import { Locator, Page } from "@playwright/test";
import BasePage from "./base/BasePage";

export class BookingPage extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  async visitMainPage(): Promise <void> {
    await this.page.goto('/', { timeout: 30000 });
  }
}