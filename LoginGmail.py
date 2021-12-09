from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth


class Handle():
    # 登入
    def login():
        driver.find_element_by_id("identifierId").send_keys("c1747902812@gmail.com")
        driver.find_element_by_id("identifierNext").click()
        driver.find_element_by_name("password").send_keys("c31524045c")
        driver.find_element_by_id("passwordNext").click()


if __name__ == "__main__":
    url = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow'

    webdriver.ChromeOptions().add_argument("--disable-extensions")

    webdriver.ChromeOptions().add_argument("--disable-popup-blocking")

    webdriver.ChromeOptions().add_argument("--profile-directory=Default")

    webdriver.ChromeOptions().add_argument("--ignore-certificate-errors")

    webdriver.ChromeOptions().add_argument("--disable-plugins-discovery")

    webdriver.ChromeOptions().add_argument("--incognito")

    webdriver.ChromeOptions().add_argument(
        "user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.set_window_size(400, 1000)
    driver.get(url)

    Handle.login()