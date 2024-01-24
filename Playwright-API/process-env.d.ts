export { };
declare global {
    namespace NodeJS {
        interface ProcessEnv {
            API_TOKEN: string;
            BOOKER_USERNAME: string;
            BOOKER_PASSWORD: string;
            SAUCEDEMO_URL: string;
        }
    }
}