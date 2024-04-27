import { Locator, Page } from '@playwright/test';

export default class BasePage {
    readonly page:Page;
    readonly submitButton: Locator;

    constructor(page:Page) {
        this.page = page;
        this.submitButton = this.page.locator(`xpath=//button[@id="submitContact"]`);
    }
}