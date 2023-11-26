from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://zoom:Teremok1@srvolap.sima-land.ru/Reports/powerbi/%D0%BF%D0%BB%D0%B0%D0%BD%D1%84%D0%B0%D0%BA%D1%82%D0%BD%D1%8B%D0%B9%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7")
while "Сервер отчетов" in driver.title:
    elem = driver.find_element(By.CLASS_NAME, "fill ui-role-button-fill")
    elem.click()
    driver.close()