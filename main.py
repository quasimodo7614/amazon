import argparse
import json
import os

from selenium import webdriver
import pkg.conifg
from pkg import signin
from pkg.fetch_single import fetch_amazon_product_details
from pkg.search_image import searchImage
from pkg.search_name import searchProduct


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description='Process search parameters.')

    # 添加 user 参数，必填
    parser.add_argument('--user', type=str, required=True, help='Username (required)')

    # 添加 password 参数，必填
    parser.add_argument('--password', type=str, required=True, help='Password (required)')

    # 添加 maxLink 参数，类型为 int，默认值为 3
    parser.add_argument('--maxLink', type=int, default=3, help='Maximum number of links to fetch (default: 3)')

    # 添加 searchType 参数，必选，值限制为 product 或 image
    parser.add_argument('--searchType', type=str, choices=['product', 'image'], required=True,
                        help='Type of search: product or image')

    # 添加 name 参数，但不立即设为必选
    parser.add_argument('--name', type=str, help='Name of the product (required if searchType is "product")')

    # 解析命令行参数
    args = parser.parse_args()

    # 检查如果 searchType 是 product 但没有提供 name，则报错
    if args.searchType == 'product' and not args.name:
        parser.error('The --name parameter is required when --searchType is "product".')

    # 在这里根据获取的参数执行相应的逻辑
    print(f'User: {args.user}')
    print(f'Password: {args.password}')
    print(f'maxLink: {args.maxLink}')
    print(f'searchType: {args.searchType}')
    if args.searchType == 'product':
        print(f'name: {args.name}')

    pkg.conifg.maxLink = args.maxLink
    pkg.conifg.amazonUser = args.user
    pkg.conifg.amazonPassWorld = args.password

    driver = webdriver.Chrome()
    signin.signin(driver)

    output_dir = os.getcwd()  # 获取当前目录
    all_product_details = []

    links = []
    if args.searchType == 'image':
        links = searchImage(driver)
    else:
        links = searchProduct(driver, args.name)

    # 遍历数组并调用函数
    for url in links:
        product_details = fetch_amazon_product_details(driver, url, max_retries=2)
        if product_details:
            all_product_details.append(product_details)
        else:
            print(f"无法获取 {url} 的产品详情")

    filename = os.path.join(output_dir, 'all_product_details.json')
    # 将所有产品详情的 JSON 数据保存到一个文件中
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_product_details, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
