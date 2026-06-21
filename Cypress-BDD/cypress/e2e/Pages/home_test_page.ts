class HomePage {
  visitURL(): void {
    cy.fixture("home").then((data) => {
      cy.visit(data.url);
    });
  }
  headerSection(): Cypress.Chainable<JQuery<HTMLElement>> {
    let header = cy.get("[class='panel header']");
    return header;
  }

  footerSection(): Cypress.Chainable<JQuery<HTMLElement>> {
    let footer = cy.get("[class='footer content']");
    return footer;
  }
}

export default HomePage;
