from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # ищем х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # записываем значение х в переменную
    x = x_element.text
    # высчитываем значение функции
    y = calc(x)
    # ищем поле ввода
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    # вводим значение функции в поле ввода
    answer.send_keys(y)
    time.sleep(1)
    # ищем чекбокс
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    # кликаем по чекбоксу
    robotCheckbox.click()
    time.sleep(1)
    # ищем радиобаттон и кликаем по нему
    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotsRule.click()
    time.sleep(1)
    # ищем кнопку сабмит и кликаем по ней
    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
