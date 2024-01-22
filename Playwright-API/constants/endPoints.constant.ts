const token: string = process.env.API_TOKEN;

export default class EndPoints {
    public BOOK_AUTH = '/auth';
    public MOVIE_SEARCH = `/?apikey=${token}&t=baby&y=2019&r=json&plot=full`;
}