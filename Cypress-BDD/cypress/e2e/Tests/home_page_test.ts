import { Given, Then } from "@badeball/cypress-cucumber-preprocessor";
import HomePage from "../Pages/home_test_page";

const homePage: any = new HomePage();

Given("I am on the home page", () => {
  homePage.visitURL();
});

Then("The header section should be visible", () => {
  homePage.headerSection().should("be.visible");
});

Then("The footer section should be visible", () => {
  homePage.footerSection().should("be.visible");
});
