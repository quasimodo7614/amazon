import time
import urllib
from selenium.webdriver.common.by import By

from pkg import conifg


def searchProduct(driver, product):
    encoded_product = urllib.parse.quote(product)
    url = 'https://www.amazon.com/s?k=' + encoded_product
    driver.get(url)
    time.sleep(2)

    driver.refresh()

    time.sleep(5)  # 防止页面没刷新完

    links = []
    i = 1
    try:
        # 查找所有商品的链接元素
        product_links = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-no-outline"]')

        # 打印每个商品链接的href属性
        for link in product_links:
            if i > conifg.maxLink:
                break
            try:
                links.append(link.get_attribute('href'))
                i += 1
            except:
                print("get link failed")

        return links
    except:
        print("find failed")

#
# driver = webdriver.Chrome()
# signin.signin(driver)
# links = searchProduct(driver, "macbook")
#
# print("link is: ", links)
#
# output_dir = os.getcwd()  # 获取当前目录
# all_product_details = []
# # 遍历数组并调用函数
# for url in links:
#     product_details = single.fetch_amazon_product_details(driver, url, max_retries=2)
#     if product_details:
#         # print(product_details)
#         all_product_details.append(product_details)
#     else:
#         print(f"无法获取 {url} 的产品详情")
#
# filename = os.path.join(output_dir, 'all_product_details.json')
# # 将所有产品详情的 JSON 数据保存到一个文件中
# with open(filename, 'w', encoding='utf-8') as f:
#     json.dump(all_product_details, f, ensure_ascii=False, indent=4)
