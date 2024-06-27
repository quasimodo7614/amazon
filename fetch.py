import json
import time
import urllib
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

import single

# product = "table"
# encoded_product = urllib.parse.quote(product)

url = 'https://www.amazon.com/s?k=' + encoded_product

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

driver.refresh()

time.sleep(5)  # 防止页面没刷新完

try:

    # 查找商品元素
    items = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

    hrefs = []

    # 遍历所有搜索结果项
    for item in items:
        # 尝试获取每个item中的a标签的href属性
        try:
            link_element = item.find_element(By.XPATH,
                                             './/a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
            href = link_element.get_attribute('href')
            hrefs.append(href)
        except Exception as e:
            # 如果出现异常，可以选择打印异常信息或忽略
            print(f"Error: {e}")

    # 打印所有的href
    print(len(hrefs))
    # 遍历子集
    maxRef = 3
    output_dir = os.getcwd()  # 获取当前目录
    all_product_details = []  # 用于存储所有产品详情

    for url in hrefs:
        if maxRef <= 0:
            break
        product_details = single.fetch_amazon_product_details(url, max_retries=3)
        all_product_details.append(product_details)  # 将每个产品详情添加到列表中
        maxRef -= 1
    filename = os.path.join(output_dir, 'all_product_details.json')

    # 将所有产品详情的 JSON 数据保存到一个文件中
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_product_details, f, ensure_ascii=False, indent=4)

finally:
    time.sleep(50)
    # 关闭浏览器
    driver.quit()
