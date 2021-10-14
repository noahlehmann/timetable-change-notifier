import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Bot:

    def __init__(self, url, program, semester):
        self.url = url
        self.program = program
        self.semester = semester

    def check_changes(self):

        # browser init and call product url
        browser = None
        while browser is None:
            try:
                browser = webdriver.Remote("http://selenium:4444", DesiredCapabilities.FIREFOX)
            except:
                browser = None
                retry_interval = 10
                print(f"could not connect to remote server, trying again in {retry_interval} s")
                time.sleep(retry_interval)

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
                time.sleep(10)
                Select(semester).select_by_visible_text(self.semester)

                time.sleep(10)
                changes = browser.find_element_by_id('vorlesungen')

                if "Ersatztermin".lower() in str(changes.text).lower():
                    print("changes found")
                    # send email notification
                    # Alert.email_alert(browser.title + " is available !!!", browser.current_url)
                    browser.quit()
                    break
                else:
                    print("refreshing")
                    browser.execute_script("location.reload(true);")
                    time.sleep(5)
            except:
                print("Problems while reading page")
                browser.execute_script("location.reload(true);")
