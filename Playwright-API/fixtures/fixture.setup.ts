import * as dotenv from 'dotenv';
dotenv.config();
import test from '@playwright/test';
import Login from '../pages/loginpage.class';


export const baseTest = test.extend<
{login: Login } & 
{ baseURL: string }>({
    baseURL: async({}, use) => {
        await use(process.env.SAUCEDEMO_URL)
    },
    login: async ({baseURL}, use) => {
        const login: Login = new Login(baseURL)
        await use(login)
    }
})