from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def first_task():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.ID, "submit_button")
        button.click()
    finally:
        time.sleep(30)
        browser.quit()


def second_task():
    link = " http://suninjuly.github.io/find_link_text"
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        new_link = browser.find_element(By.LINK_TEXT, text)
        new_link.click()
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


def third_task():
    link = "http://suninjuly.github.io/huge_form.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        for area in browser.find_elements(By.TAG_NAME, "input"):
            area.send_keys("1")
        browser.find_element(By.CLASS_NAME, "btn-default").click()
    finally:
        time.sleep(30)
        browser.quit()


def fourth_task():
    link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()


def registration(link):
    """Write your registration link as argument of this function"""
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        # Селектор должен находить только 1 значение. Из-за для этого добавлены [attribute=value]
        first_name_input = browser.find_element(By.CSS_SELECTOR, '.first[placeholder="Input your first name"]')
        first_name_input.send_keys("Fedor")
        last_name_input = browser.find_element(By.CSS_SELECTOR, '.second[placeholder="Input your last name"]')
        last_name_input.send_keys("Kuznetsov")
        email_input = browser.find_element(By.CSS_SELECTOR, '.third[placeholder="Input your email"]')
        email_input.send_keys("fake@mail.ru")
        # Кнопку не обязательно искать по селектору
        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()
        result = browser.find_element(By.TAG_NAME, "h1")
        assert "Congratulations! You have successfully registered!" == result.text
    finally:
        time.sleep(30)
        browser.quit()


def fifth_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/math.html")
        value = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        for box in browser.find_elements(By.CLASS_NAME, "form-check-label"):
            box.click()
        browser.find_element(By.CLASS_NAME, "btn-default").click()
    finally:
        time.sleep(20)
        browser.quit()


def sixth_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/get_attribute.html")
        value = browser.find_element(By.ID, "treasure").get_attribute("valuex")
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        for id_ in ("robotCheckbox", "robotsRule"):
            browser.find_element(By.ID, id_).click()
        browser.find_element(By.CLASS_NAME, "btn-default").click()
    finally:
        time.sleep(20)
        browser.quit()


def seventh_task():
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/selects1.html?")
        sum = 0
        for num in ("num1", "num2"):
            sum += int(browser.find_element(By.ID, num).text)
        select = Select(browser.find_element(By.ID, "dropdown"))
        select.select_by_value(str(sum))
        browser.find_element(By.CLASS_NAME, "btn-default").click()
    finally:
        time.sleep(20)
        browser.quit()


def eighth_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    try:
        browser = webdriver.Chrome()
        link = "http://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        value = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        button = browser.find_element(By.CLASS_NAME, "btn-primary")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        for box in browser.find_elements(By.CLASS_NAME, "form-check-label"):
            box.click()
        button.click()

    finally:
        time.sleep(20)
        browser.quit()


def ninth_task():
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)
        for field, value in zip(browser.find_elements(By.CLASS_NAME, "form-control"), ("Fedor", "Kuznetsov", "fake@mail.ru")):
            field.send_keys(value)
        browser.find_element(By.ID, "file").send_keys("/home/fedor/Рабочий стол/Selenium/file.txt")
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
    finally:
        time.sleep(20)
        browser.quit()


def tenth_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/alert_accept.html")
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
        browser.switch_to.alert.accept()
        value = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
    finally:
        time.sleep(20)
        browser.quit()


def eleventh_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/redirect_accept.html")
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
        browser.switch_to.window(browser.window_handles[1])
        value = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
    finally:
        print(browser.switch_to.alert.text)
        browser.quit()


def twelfth_task():
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    try:
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        browser.find_element(By.ID, "book").click()
        value = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(value))
        browser.find_element(By.ID, "solve").click()
    finally:
        print(browser.switch_to.alert.text)
        browser.quit()


if __name__ == "__main__":
    # Run current task solution below
    pass
