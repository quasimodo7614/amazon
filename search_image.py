import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 使用文件选择器来选择文件
from tkinter import Tk
from tkinter.filedialog import askopenfilename


import signin
import single

maxLink = 3  # 根据图片搜索，相关图片最多展示6条，可配置，todo: 不要在代码中写死


def searchImage(driver):
    driver.get("https://www.amazon.com/stylesnap")
    time.sleep(2)
    driver.refresh()  # 主要是因为第一次会要求输入验证码，直接 refresh 一下可以访问 todo: 判断某些元素是不是有了，有了就可以，没有继续刷新
    time.sleep(5)

    try:

        file_input = driver.find_element(By.ID, 'file')
        file_input.send_keys(file_path)
        driver.implicitly_wait(10)

        links = []
        i = 1
        try:
            # 查找所有 <a> 标签
            linksRaw = driver.find_elements(By.CSS_SELECTOR, 'a.item-details[data-testid="productCellImage"]')
            # 提取并打印所有链接的 href 属性
            for link in linksRaw:
                if i > maxLink:
                    break
                href = link.get_attribute('href')
                links.append(href)
                i += 1
        except:
            print("get link error")
        return links

    except Exception as e:
        print(f"An error occurred when click: {e}")




 # 创建Tkinter根窗口
root = Tk()
root.withdraw()  # 隐藏根窗口
# 弹出文件选择对话框，限制文件类型为图片
file_path = askopenfilename()
root.destroy()




driver = webdriver.Chrome()
signin.signin(driver)
links = searchImage(driver)

output_dir = os.getcwd()  # 获取当前目录
all_product_details = []

# 遍历数组并调用函数
for url in links:
    product_details = single.fetch_amazon_product_details(driver, url, max_retries=2)
    if product_details:
        # print(product_details)
        all_product_details.append(product_details)
    else:
        print(f"无法获取 {url} 的产品详情")

filename = os.path.join(output_dir, 'all_product_details.json')
# 将所有产品详情的 JSON 数据保存到一个文件中
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_product_details, f, ensure_ascii=False, indent=4)

