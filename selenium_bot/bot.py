from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from alert import Alert


class Bot:

    def __init__(self, url, program, semester):
        self.url = url
        self.program = program
        self.semester = semester

    def check_product_by_name(self):
        # browser settings
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)

        # browser init and call product url
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(self.url)

        try:
            # find search bar type the name of product and press enter
            searchbar = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.NAME, 'tx_stundenplan_stundenplan[studiengang]'))
                    )
            searchbar.send_keys(self.program)
            searchbar.send_keys(Keys.RETURN)

            # find link to required product
            link_to_product = WebDriverWait(browser, 10).until(
                        EC.presence_of_all_elements_located((By.LINK_TEXT, self.name))
                    )

            # navigate to href from product
            for link in link_to_product:
                if link.text == self.name:
                    link.send_keys(Keys.ENTER)
                    break

            while True:
                try:
                    # check if buy button is available with 10 sec page loading time
                    WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.ID, 'availability'))
                    )

                    print("Product is available")
                    # send email notification
                    # Alert.email_alert(browser.title + " is available !!!", browser.current_url, self.email)
                    browser.quit()
                    break
                except:
                    print("Product is not available")
                    # reload browser and try again
                    browser.execute_script("location.reload(true);")
        except:
            print("Product is not available")
            # reload browser and try again
            browser.execute_script("location.reload(true);")
