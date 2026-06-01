class HomePage {
    visitURL(){
        cy.fixture("example").then((data) => {
            cy.visit(data.url);
        });
    }
    headerSection(){
        let header = cy.get("")
        return header;
    }
}

export default HomePage;