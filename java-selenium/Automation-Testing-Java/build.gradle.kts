plugins {
    id("java")
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.9.1"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    // https://mvnrepository.com/artifact/org.testng/testng
    testImplementation("org.testng:testng:7.8.0")
    // https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java
    implementation("org.seleniumhq.selenium:selenium-java:4.16.1")
    // https://mvnrepository.com/artifact/io.github.bonigarcia/webdrivermanager
    implementation("io.github.bonigarcia:webdrivermanager:5.6.2")
}

tasks.test {
    useJUnitPlatform()
}