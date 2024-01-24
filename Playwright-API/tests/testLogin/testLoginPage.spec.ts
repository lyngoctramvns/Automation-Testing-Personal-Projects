import { expect } from '@playwright/test';
import { baseTest as test } from '../../fixtures/fixture.setup';


test.describe("Login Page Test Suite", async () => {
    test("Go to the page successfully", async({login}) => {
        const data = await login.loginInteraction();
        expect(data).toEqual('https://www.saucedemo.com/v1/index.html')
    })
})