import scrapy


class PagesSpider(scrapy.Spider):
    name = 'pages'  # 爬虫的名称，不可更改
    allowed_domains = ['formoon.github.io']  # 域名称
    start_urls = ['https://formoon.github.io/']  # 从这个网址开始执行爬虫，注意默认是http，修改成https
    # scrapy爬虫中不会主动修改页面中的链接，所以自己增加一个类变量用于将相对地址完整成为绝对地址。
    baseurl = 'https://formoon.github.io'

    def parse(self, response):
        print("zhuzhuzhuzhu")
        # scrapy爬虫主要的难点是xpath和css选择器的使用，请在网上搜索相关资源弄清楚
        # 爬虫使用相关选择器在整个html中定位自己所需要的节点及获取其中的数据
        for course in response.xpath('//ul/li'):
            # 获取文章链接
            href = self.baseurl + course.xpath('a/@href').extract()[0]
            # 获取文章标题
            title = course.css('.card-title').xpath('text()').extract()[0]
            # 获取文章发布日期
            date = course.css('.card-type.is-notShownIfHover').xpath('text()').extract()[0]
            # 显示结果
            print
            title, href, date
        for btn in response.css('.container--call-to-action').xpath('a'):
            href = btn.xpath('@href').extract()[0]
            name = btn.xpath('button/text()').extract()[0]
            # 如果屏幕上有下一页按钮，则递归访问下一页的页面
            if name == u"下一页":  # 注意python2中对于中文要显式的增加'u'前缀表示是unicode字符
                yield scrapy.Request(self.baseurl + href, callback=self.parse)