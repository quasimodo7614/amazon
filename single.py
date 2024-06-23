from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from setdeliver import test_setdeliver


def fetch_amazon_product_details(url, max_retries=3):
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式，不打开浏览器窗口
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    # 设置ChromeDriver路径
    driver = webdriver.Chrome()

    for attempt in range(max_retries):
        try:
            # 初始化WebDriver
            driver.get(url)
            time.sleep(5)  # 等待页面加载

            # 获取标题
            title = driver.find_element(By.ID, 'productTitle').text.strip()

            price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text.strip()
            # price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]').text.strip()

            # # 获取描述
            # try:
            #     # description = driver.find_element(By.XPATH,'//*[@id="bookDescription_feature_div"]/div/div[1]/span').text.strip()
            #     description = driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul').text.strip()
            # except:
            #     description = driver.find_element(By.CSS_SELECTOR,'//*[@id="feature-bullets"]/ul').text.strip()
            #     # //*[@id="aplus"]/h2
            #     # //*[@id="productDescription_feature_div"]/h2

            # 获取评分
            # rating = driver.find_element(By.XPATH, '//*[@id="acrPopover"]/span[1]/a/span').text.strip()
            #
            # image_element = driver.find_element(By.ID, "imgTagWrapperId").find_element(By.TAG_NAME, "img")
            # image_url = image_element.get_attribute("src")

            # 打印结果
            print("标题:", title)
            print("价格:", price)
            # print("描述:", description)
            # print("评分:", rating)
            # print("图片:", image_url)

            # 关闭浏览器
            # driver.quit()

            # 返回结果
            return {
                "title": title,
                "price": price,
                # "description": description,
                # "rating": rating,
                # "image": image_url
            }
        except Exception as e:
            print(f"尝试 {attempt + 1} 失败: {e}")
            driver.refresh()
            time.sleep(2)
            if attempt == max_retries - 1:
                print("多次尝试后仍然失败，退出程序。")
                return None


# 示例数组
urls = [
    "https://www.amazon.com/dp/B01N4KYKNY/ref=mweb_up_am_fl_st_na_un_up_sm_vs_lns",
    # "https://www.amazon.com/Hanpceirs-Sundress-Vintage-Cocktail-Dresses/dp/B0CSMMDNR1/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.Altj2qxxKNbsGuhRkwcpP8-3EA_PJaVAF-WWm4-7gRM.W61XUPguLEgCe7DlpzL8ecOKY5SWQvdY_a9ydNHZf04&dib_tag=se&keywords=%E5%A4%8F%E5%A4%A9%E8%BF%9E%E8%A1%A3%E8%A3%99&qid=1719157467&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    # 添加更多URL
]

driver = webdriver.Chrome()
# 遍历数组并调用函数
for url in urls:

    product_details = fetch_amazon_product_details(url, max_retries=2)
    if product_details:
        print(product_details)
    else:
        print(f"无法获取 {url} 的产品详情")

