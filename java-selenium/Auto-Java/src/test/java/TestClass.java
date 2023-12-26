import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestClass {
    ChromeDriver chromeDriver;
    @BeforeMethod
    public void beforeTest(){
        WebDriverManager.chromedriver().setup();
        chromeDriver = new ChromeDriver();
    }
    @Test
    public void RunTest(){
        chromeDriver.get("https://www.saucedemo.com/");
    }

    @Test
    public void RunTest2(){
        System.out.println("Hello TestNG 2");
    }

    @AfterMethod
    public void afterTest(){

    }
}
