import { Given, When, Then, And } from "cypress-cucumber-preprocessor/steps";
import HomePage from "../Pages/home_test_page.cy";

const homePage = new HomePage();

Given("I am on the home page", () => {
  homePage.visitURL();
});