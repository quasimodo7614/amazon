import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def signin(driver):
    driver.get("https://www.amazon.com/")
    time.sleep(2)
    driver.refresh()
    time.sleep(5)

    try:
        # 等待按钮元素出现，最多等待10秒
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nav-link-accountList"]'))
        )
        # 点击按钮
        button.click()
        try:
            # print("abc")
            # 等待文本输入框出现，最多等待10秒
            input_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ap_email"]'))
            )
            # 在文本输入框中输入值
            input_box.send_keys('8618310063609')

            # 等待提交按钮出现，最多等待10秒
            continue_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
            )
            continue_button.click()
            pass_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ap_password"]'))
            )
            # 在文本输入框中输入值
            pass_box.send_keys('wszze7614')

            # 等待提交按钮出现，最多等待10秒
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="signInSubmit"]'))
            )
            # 点击提交按钮
            submit_button.click()

        except Exception as e:
            print(f"An error occurred when submmit: {e}")
    except Exception as e:
        print(f"An error occurred when click: {e}")




