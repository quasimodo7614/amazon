# 准备工作
1. 使用了 https://www.selenium.dev/documentation/webdriver/interactions/
2. 最好能够先实验 selenium 的简单例子。这里需要安装 python3.
3. pip install selenium (如果不了解 pip 是啥，需要先了解 python 的包管理工具 pip)

# 代码架构
pkg 是实际业务逻辑

- config 是集中的参数配置
- fetch_single 是单个页面 fetch 的函数，主要获取详情页的 价格，图片，描述等
- search_image 是根据 image 搜索，需要提前将图片下载到本地
- search_name 是根据商品 name 搜索
- signin 是模拟登录的逻辑

# 参数说明

--user 必填，模拟 amazon 登录的用户名，不登录有的商品无法获取价格。

--password  必填，模拟 amazon 登录的密码，不登录有的商品无法获取价格。

--maxLink 选填，默认为 3

--searchType 搜索类型，product 为根据产品名搜索， image 为 根据图片搜索

--name 当searchType=product 是必填，其他情况选填。


运行示例：
```angular2html
 python main.py --user=8612345678910 --password=xxx --searchType=product --name=iphone
```

```angular2html
 python main.py --user=8612345678910 --password=xxx --searchType=image

```


# 注意
1. 测试会有失败，关闭重来即可，后续可以优化。
2. 不要过于频繁操作，会引发 amazon 的发爬虫或者其他机制。

