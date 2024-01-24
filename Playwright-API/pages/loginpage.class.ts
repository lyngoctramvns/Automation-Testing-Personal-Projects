import { webkit } from '@playwright/test';


export default class Login {
private baseURL: string;

    constructor ( baseURL: string ){
        this.baseURL = baseURL
    }

    async loginInteraction(): Promise< String >{
        const browser = await webkit.launch();
        const context = await browser.newContext();
        const page = await context.newPage()
        await page.goto(this.baseURL);
        await browser.close();
        return this.baseURL
    }
    
}