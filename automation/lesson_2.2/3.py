from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = num2.text
    summary = int(x) + int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summary))
    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
