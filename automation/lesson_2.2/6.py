from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # высчитываем значение функции
    y = calc(x)
    # ищем поле ввода
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    # ищем чекбокс
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", robotCheckbox)
    # кликаем по чекбоксу
    robotCheckbox.click()
    # ищем радиобаттон и кликаем по нему
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    # ищем кнопку сабмит и кликаем по ней
    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
