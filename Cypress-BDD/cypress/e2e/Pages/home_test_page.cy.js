class HomePage {
    visitURL(){
        cy.fixture("example").then((data) => {
            cy.visit(data.url);
        });
    }
}

export default HomePage;