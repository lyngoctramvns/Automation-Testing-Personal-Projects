import * as dotenv from "dotenv";
dotenv.config();
import { test, expect} from '@playwright/test';
const token = process.env.API_TOKEN;


test('Get movies according to year - 2019', async ({request}) => {
    const response = await request.get(`/?apikey=${token}&t=a&y=2019&plot=full`);
    console.log(await response.json());
    expect(response.ok()).toBeTruthy();
    expect(response.status()).toBe(200);
});

