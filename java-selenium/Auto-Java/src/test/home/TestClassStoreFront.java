import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestClassStoreFront {
    ChromeDriver chromeDriver;
    @BeforeMethod
    public void beforeTest(){
        WebDriverManager.chromedriver().setup();
        chromeDriver = new ChromeDriver();
    }
    @Test
    public void GoToHome(){
        chromeDriver.get("https://www.saucedemo.com/");
        sleep(5000);
    }

    @AfterMethod
    public void afterTest(){
        chromeDriver.quit();
    }
    private void sleep(int time){
        try{
            Thread.sleep(time);
        } catch(Exception ex){
            System.out.println(ex.getMessage());
        }
    }
}
