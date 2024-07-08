import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def fetch_amazon_product_details(driver, url, max_retries=3):
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式，不打开浏览器窗口
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    # 设置ChromeDriver路径

    for attempt in range(max_retries):
        try:
            # 初始化WebDriver
            driver.get(url)
            time.sleep(2)
            driver.refresh()

            title = driver.find_element(By.ID, 'productTitle').text.strip()
            # print("title is: ", title)

            price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text.strip()
            if price == "":
                price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]').text.strip()

            # fiveitem
            try:
                fiveitem = driver.find_element(By.XPATH, '//*[@id="feature-bullets"]/ul').text.strip()
            except:
                fiveitem = ""
            # print("fiveitem is: ", fiveitem)

            try:
                prodDetails = driver.find_element(By.XPATH, '//*[@id="prodDetails"]/div').text.strip()
            except:
                prodDetails = ""
            # print("prodDetails is: ", prodDetails)

            try:
                productDescription = driver.find_element(By.ID, 'productDescription').text.strip()
                # //*[@id="productDescription"]
            except:
                productDescription = ""
            # print("productDescription is: ", productDescription)

            imageList = []
            try:

                # 找到所有图片的元素
                images = driver.find_elements(By.CSS_SELECTOR, "ul.a-button-list img")

                # 遍历并点击每个图片, 不点击不会加载，只能获取到一张图片
                for image in images:
                    try:
                        # 通过 ActionChains 移动到图片并点击
                        actions = ActionChains(driver)
                        actions.move_to_element(image).click().perform()
                    except:
                        # 出错不管
                        print("click image failed")

                # 开始获取图片列表
                ul_element = driver.find_element(By.XPATH, '//*[@id="main-image-container"]/ul')
                img_elements = ul_element.find_elements(By.TAG_NAME, 'img')
                imageList = [img.get_attribute('src') for img in img_elements]

            except:
                print("获取 image 失败")
            # print("imageList is: ", imageList)
            # time.sleep(5000)

            # 返回结果
            return {
                "link": url,
                "title": title,
                "price": price,
                "fiveitem": fiveitem,
                "prodDetails": prodDetails,
                "productDescription": productDescription,
                "image": imageList
            }
        except Exception as e:
            print(f"尝试 {attempt + 1} 失败: {e}")
            driver.refresh()
            time.sleep(2)
            if attempt == max_retries - 1:
                print("多次尝试后仍然失败，退出程序。")
                return None
#
# # 示例数组
# urls = [
#      # "https://www.amazon.com/dp/B08PZJN7BD?aref=N1GKbwWP6d&aaxitk=5f4a4fd0be1fd3eab1809bed4201e3ed&language=en_US&pd_rd_plhdr=t&smid=ATVPDKIKX0DER&ref=dacx_dp_591637243630818197_582668263125716884"
#     # 添加更多URL
#      "https://www.amazon.com/-/zh/dp/B07RV58W46/ref=sr_1_3?dib=eyJ2IjoiMSJ9.5yEcZQrh3Y7jYmCgksul88jsV2dnGhHyXM-JZfqxozId_GXJgkBfcZ9cuc9mk5cOoUFjIJ96w-hhCEbjJhWGMUCGm5-XxP2ID3fvrhwjF2UnkEwe7a9VCVtedGcKSi-mMC7-n0ihqVgEYB2NND7-p7720pZxSuKCKQ4ICkiVUzg8ci5_erCy6PybmlC1Q7rHr_ZMAVV2AD8eaESvQtHDlzhW7UxXU7YRX0iTL74mhL8.qoLIixEgW9i8bvDkfJQ1ff8tvl3i920XxMDAJL2EKoc&dib_tag=se&keywords=iphone&qid=1719504369&sr=8-3"
# ]
#
# driver = webdriver.Chrome()
# # signin.signin(driver)
# #
# # 遍历数组并调用函数
# for url in urls:
#     product_details = fetch_amazon_product_details(driver, url, max_retries=2)
#     if product_details:
#         print(product_details)
#     else:
#         print(f"无法获取 {url} 的产品详情")
