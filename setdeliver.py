import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_setdeliver(driver):
    driver.get("https://www.amazon.com/")
    time.sleep(2)
    driver.refresh()
    time.sleep(5)

    try:
        # 等待按钮元素出现，最多等待10秒
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nav-main"]/div[1]/div/div/div[3]/span[2]/span/input'))
        )
        # 点击按钮
        button.click()
        try:
            # print("abc")
            # 等待文本输入框出现，最多等待10秒
            input_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="GLUXZipUpdateInput"]'))
            )
            # 在文本输入框中输入值
            input_box.send_keys('10001')

            # 等待提交按钮出现，最多等待10秒
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="GLUXZipUpdate"]/span/input'))
            )
            # 点击提交按钮
            submit_button.click()
            finish_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/button'))
            )
            finish_button.click()

        except Exception as e:
            print(f"An error occurred when submmit: {e}")
    except Exception as e:
        print(f"An error occurred when click: {e}")


# 设置ChromeDriver路径
driver = webdriver.Chrome()
test_setdeliver(driver)
driver.refresh()
