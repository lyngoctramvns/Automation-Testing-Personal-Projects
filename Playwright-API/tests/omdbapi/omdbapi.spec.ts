import * as dotenv from "dotenv";
dotenv.config();
import { test, expect} from '@playwright/test';
const token:any = process.env.API_TOKEN;


test('Get movies according to year - 2019', async ({request}) => {
    const response = await request.get(`/?apikey=${token}&t=baby&y=2019&r=json&plot=full`);
    const responseBody = await response.json();
    expect(response.ok()).toBeTruthy();
    expect(response.status()).toBe(200);
    expect(responseBody).toHaveProperty("Title","Baby");
    expect(responseBody).toHaveProperty("Year","2019");
    expect(responseBody).toHaveProperty("Director");
    expect(responseBody).toHaveProperty("Writer");
    expect(responseBody).toHaveProperty("Actors");
    expect(responseBody).toHaveProperty("Plot");
});

