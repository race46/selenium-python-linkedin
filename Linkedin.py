from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


def fill(xpath, text):
    try:
        time.sleep(0.1)
        wb.find_element_by_xpath(xpath).send_keys(text)
    except wb.error_handler:
        fill(xpath, text)


def find_xpath(xpath):
    for i in range(50):
        try:
            time.sleep(0.1)
            return wb.find_elements_by_class_name(xpath)
        except:
            pass


wb = webdriver.Chrome("./chromedriver")
wb.maximize_window()

wb.get("https://www.linkedin.com/login")

fill("//*[@id='username']", "e-mail")
fill("//*[@id='password']", "password")
fill("//*[@id='password']", Keys.ENTER)

wb.get("https://www.linkedin.com/search/results/people/?keywords=software&origin=CLUSTER_EXPANSION&page=" + str(
    random.randint(1, 46)))

users = find_xpath("artdeco-button__text")

for user in users:
    try:
        if user.text == 'Bağlantı Kur':
            user.click()
            time.sleep(0.5)
            webdriver.ActionChains(wb).send_keys(Keys.TAB).perform()
            webdriver.ActionChains(wb).send_keys(Keys.TAB).perform()
            webdriver.ActionChains(wb).send_keys(Keys.TAB).perform()
            webdriver.ActionChains(wb).send_keys(Keys.ENTER).perform()
            time.sleep(0.5)
    except:
        pass
wb.close()
