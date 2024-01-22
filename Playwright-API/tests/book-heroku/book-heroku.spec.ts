import * as dotenv from "dotenv";
dotenv.config();
import { test, expect} from '@playwright/test';
import EndPoints from "../../constants/endPoints.constant";
const authen = new EndPoints().BOOK_AUTH
const username = process.env.BOOKER_USERNAME;
const password = process.env.BOOKER_PASSWORD;

test('Test authentication', async({request})=> {
    const response = await request.post(authen, {
        headers: {
            'Content-Type':'application/json'
        },
        data: {
            "username": username,
            "password": password
        }
    })
    const responseBody = await response.json();
    expect(response.ok()).toBeTruthy();
    expect(response.status()).toBe(200);
    expect(responseBody).toHaveProperty("token");
})