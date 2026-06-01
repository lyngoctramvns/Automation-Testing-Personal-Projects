class HomePage {
    visitURL(){
        cy.fixture("example").then((data) => {
            cy.visit(data.url);
        });
    }
    headerSection(){
        let header = cy.get("[class='panel header']");
        return header;
    }

    footerSection(){
        let footer = cy.get("[class='footer content']");
        return footer;
    }
}

export default HomePage;