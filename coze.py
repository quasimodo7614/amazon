import requests
import json

# 设置请求的 URL
url = "https://api.coze.com/open_api/v2/chat"

# 准备请求头
headers = {
    'Authorization': 'Bearer pat_4Ova92hn4sY2VHcDZzPJDLyNmL8ZHTOCiizPg9Dbk4dzQ5ePJzdB4CinLqRTxrAk',
    # 替换 {Personal_Access_Token} 为你的个人访问令牌
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Connection': 'keep-alive',
}

jsonData = '[{\"title\":\"Online Gym Shop CB18891 Outdoor Garden Lounge Set - Poly Rattan44; White - 15 Piece\",\"price\":\"566\",\"fiveitem\":\"Rattan color: White\\nCushion color: Black\\nMaterial: Powder-coated steel frame + tempered glass table top\\nCushion material: 100% Polyester\\nCorner sofa dimensions: 28 x 28 x 25 (W x D x H)\",\"prodDetails\":\"Technical Details\\nAssembly Required Yes\\nShape L-Shape\\nItem dimensions L x W x H 33.5 x 70 x 63 inches\\nProduct Care Instructions Wipe with Sofa Cloth\\nMaterial Coated,Glass,Steel\\nManufacturer OnlineGymShop.com\\nItem Weight 114.6 pounds\\nProduct Dimensions 33.5 x 70 x 63 inches\\nItem model number 42093\\nAssembled Height 63 inches\\nAssembled Width 33.5 inches\\nAssembled Depth 70 inches\\nAdditional Information\\nASIN B01N4KYKNY\\nDate First Available March 15, 2018\\nWarranty & Support\\nAmazon.com Return Policy:Regardless of your statutory right of withdrawal, you enjoy a 30-day right of return for many products. For exceptions and conditions, see Return details.\\nProduct Warranty: For warranty information about this product, please click here\\nFeedback\\nWould you like to tell us about a lower price?\",\"productDescription\":\"This rattan patio lounge set combines style and functionality, and will become the focal point of your garden or patio. The whole furniture set is designed to be used outdoors year-round.\\nThanks to the weather-resistant and waterproof PE rattan, the lounge set is easy to clean, hard-wearing and suitable for daily use. The lounge set features a sturdy powder-coated steel frame, which is highly durable. It is also lightweight and modular, which makes it completely flexible and easy to move around to suit any setting. The thick, removable cushions are highly comfortable and easy to wash.\\nDelivery includes 1 corner sofa, 2 center sofas, 2 ottomans, 1 tea table, 5 seat cushions and 4 back cushions.\\nNote 1): We recommend covering the set in the rain, snow and frost.\\nNote 2): This item will be shipped flat packed. Assembly is required; all tools, hardware and instructions are included.\\nRattan color: White\\nCushion color: Black\\nMaterial: Powder-coated steel frame + tempered glass table top\\nCushion material: 100% Polyester\\nCorner sofa dimensions: 28″ x 28″ x 25″ (W x D x H)\\nCenter sofa dimensions: 28″ x 28″ x 25″ (W x D x H)\\nOttoman dimensions: 28″ x 28″ x 12″ (L x W x H)\\nTable dimensions: 29″ x 29″ x 12″ (L x W x H)\\nCushion thickness: 2″\\nDelivery includes:\\n1 x Corner sofa\\n2 x Center sofa\\n2 x Ottoman\\n1 x Tea table\\n5 x Seat cushion\\n4 x Back cushion\\nWARNING Cushion and pad are only for outdoor use. Do not take them inside of dwelling\",\"image\":[\"https://m.media-amazon.com/images/I/41Yya7NSi+S._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/61fQ5EUoucL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/414hvDlDTfL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/51l0M9lQHdL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/51U3ZiWHWbL._AC_SX679_.jpg\"]},{\"title\":\"[New and Comfy Furniture Set - Outdoor Lounge and Rattan Set with Cushioned Chairs - White Garden Furniture for Relaxation-White\",\"price\":\"971\",\"fiveitem\":\"outdoor relaxation: Unwind in style with this luxurious furniture set featuring cushioned chairs, providing comfort for lounging and leisure in your garden or outdoor space.\\nStylish and durable rattan design: Crafted with a rattan weave, this outdoor lounge set showcases an elegant white garden furniture aesthetic that complements any outdoor decor while offering-lasting durability.\\nVersatile and functional: This versatile rattan set is perfect for hosting gatherings, enjoying meals al fresco, or simply lounging in the sun. Its cushioned chairs provide the spot for relaxation, making it a must-have addition to your outdoor living area.\\nAll-weather performance: Designed to withstand various weather conditions, this furniture set is built to last and can be left outdoors year-round. The weather-resistant materials ensure that you can enjoy its beauty and functionality for years to come.\\nEasy maintenance: With its easy-to-clean and removable cushion covers, maintaining this comfortable outdoor lounge set is hassle-free. Spend less upkeep and more enjoying the tranquility of your outdoor oasis.\",\"prodDetails\":\"Technical Details\\nProduct Dimensions 0.39 x 0.39 x 0.39 inches\\nCountry of Origin China\\nItem model number WHLW887172\\nAdditional Information\\nASIN B0CHXLMTD2\\nDate First Available September 12, 2023\\nWarranty & Support\\nAmazon.com Return Policy:Regardless of your statutory right of withdrawal, you enjoy a 30-day right of return for many products. For exceptions and conditions, see Return details.\\nProduct Warranty: For warranty information about this product, please click here\\nFeedback\\nWould you like to tell us about a lower price?\",\"productDescription\":\"Introductions:\\nIntroducing our brand-new furniture set, designed for relaxation in your outdoor oasis\\nThis outdoor lounge set features a stylish rattan design, adding a of elegance to any garden or space\\nCrafted from durable materials, this white garden furniture is built to withstand the and provide-lasting comfort\\nThe set includes cushioned chairs, ensuring coziness during your outdoor gatherings\\nUpgrade your outdoor living area with this comfortable and stylish rattan set today!\\nSpecifications:\\nRattan color: White\\nCushion color: Black\\nMaterial: Powder-coated steel frame + tempered glass table top\\nCushion material: Polyester\\nCorner sofa: 28 x 28 x 25 (W x x H)\\nCenter sofa: 28 x 28 x 25 (W x x H)\\nOttoman: 28 x 28 x2 (L x W x H)\\nTable: 29 x 29 x2 (L x W x H)\\nCushion thickness: 2\\nDelivery includes:\\n3 x Corner sofa\\n3 x Center sofa\\n7 x cushion\\n9 x Back cushion\\nWARNING Cushion and pad are only for outdoor use. Do not take them inside of dwelling\\nCalifornia Proposition 65\\nWarning: Cancer and Reproductive Harm ??? www.P65Warnings.ca.gov.\\n\\nVariant theme:\\nWhite\",\"image\":[\"https://m.media-amazon.com/images/I/418si8ZQDeL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/419XqNQVYIL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/61iMS6YDNaL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/61brddZl0aL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/41nz+i0CueL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/61OnS2TG4XL._AC_SX679_.jpg\",\"https://m.media-amazon.com/images/I/51YHSEfp7HL._AC_SX679_.jpg\"]}]'
# 指定文件路径
file_path = 'all_product_details.json'

# 读取文件
# with open(file_path, 'r', encoding='utf-8') as file:
    # 读取文件内容到一个字符串
    # file_content = file.read()
    # print(file_content.strip())

# 准备请求体
data = {
    "conversation_id": "",  # 会话ID，可以是任意字符串，如果需要区分对话上下文可以指定
    "bot_id": "7385059202659794961",  # 替换 {Bot_Id} 为你的机器人ID
    "user": "zengzeen",  # 用户ID或者用户名
    "query": jsonData,  # 发送给机器人的查询文本
    "stream": False,  # 设置为 False 以使用非流式响应
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查响应
if response.status_code == 200:
    print("请求成功！")
    # 解析响应内容
    response_data = response.json()
    print("响应内容：", json.dumps(response_data, indent=4, ensure_ascii=False))
else:
    print("请求失败，状态码：", response.status_code)
