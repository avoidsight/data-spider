import scrapy, pymysql

from dataSpider.items import DataspiderItem


class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
        # 获取网站标题
        context = response.xpath('/html/head/title/text()')

        # 提取网站标题
        title = context.extract_first()
        print(title)
        # filename = "teacher.html"
        # open(filename, 'w').write(response.body.decode())
        # 存放老师信息的集合
        items = []
        index = 0
        for each in response.xpath("//html/body/div[1]/div[5]/div[2]/div[4]/ul/li"):
            index = index + 1
            # print("查尔门哈", index)
            # 将我们得到的数据封装到一个 `DataspiderItem` 对象
            item = DataspiderItem()

            # extract()方法返回的都是unicode字符串
            name = each.css(".li_txt").xpath("h3/text()").extract()[0]
            title = each.css(".li_txt").xpath("h4/text()").extract()[0]
            info = each.css(".li_txt").xpath("p/text()").extract()[0]

            # xpath返回的是包含一个元素的列表
            item['name'] = name
            item['title'] = title
            item['info'] = info

            print(name, title, info)
            items.append(item)
        # appenditem = DataspiderItem()
        # item['name'] = '查鹏'
        # item['title'] = 'eng'
        # item['info'] = 'ct'
        # items.append(item)
        # 直接返回最后数据
        return items
