import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class Bot:

    def __init__(self, url, program, semester):
        self.url = url
        self.program = program
        self.semester = semester

    def check_changes(self):

        # browser init and call product url
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser.get(self.url)
        accepted_cookies = False
        while True:
            try:
                if not accepted_cookies:
                    cookie_button = WebDriverWait(browser, 10).until(
                        ec.presence_of_element_located((By.ID, 'uc-btn-deny-banner'))
                    )
                    cookie_button.click()
                    accepted_cookies = True

                program = browser.find_element_by_name('tx_stundenplan_stundenplan[studiengang]')
                Select(program).select_by_visible_text(self.program)
                semester = browser.find_element_by_id('semesterSelect')
                time.sleep(2)
                Select(semester).select_by_visible_text(self.semester)

                time.sleep(2)
                changes = browser.find_element_by_id('vorlesungen')

                if "Ersatztermin".lower() in str(changes.text).lower():
                    print("changes found")
                    # send email notification
                    # Alert.email_alert(browser.title + " is available !!!", browser.current_url, self.email)
                    browser.quit()
                    break
                else:
                    browser.execute_script("location.reload(true);")
                    time.sleep(5)
            except:
                print("Problems while reading page")
                browser.execute_script("location.reload(true);")
