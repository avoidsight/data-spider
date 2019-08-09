import scrapy, pymysql

from dataSpider.MusicItem import MusicItem
from dataSpider.items import DataspiderItem


class Opp2Spider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ("https://music.163.com/#/playlist?id=2829883282",)

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
        for each in response.xpath("//*[@id='auto-id-0HHHz6e9x1PTB0x4']/table/tbody"):
            index = index + 1
            # print("查尔门哈", index)
            # 将我们得到的数据封装到一个 `DataspiderItem` 对象
            item = MusicItem()

            # extract()方法返回的都是unicode字符串
            name = each.css(".txt").xpath("td[2]/div/div/div/span/a/b").extract()[0]
            singer = each.css(".text").xpath("td[4]/div/span/a").extract()[0]
            time = each.css(".u-dur ").xpath("td[3]/span").extract()[0]

            # xpath返回的是包含一个元素的列表
            item['name'] = name
            item['singer'] = singer
            item['time'] = time

            print(name, singer, time)
            items.append(item)
        # appenditem = DataspiderItem()
        # item['name'] = '查鹏'
        # item['title'] = 'eng'
        # item['info'] = 'ct'
        # items.append(item)
        # 直接返回最后数据
        return items
