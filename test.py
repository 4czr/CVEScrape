import scrapy
import HTMLParser


class Download(scrapy.Spider):
    name = 'Download'
    allowed_domains = ['exploit-db.com']
    start_urls = [

        'https://www.exploit-db.com/webapps/',
        'https://www.exploit-db.com/remote/',
        'https://www.exploit-db.com/local/',
        'https://www.exploit-db.com/dos/'
    ]

    def parse(self, response):
        # print response.url
        selector = scrapy.Selector(response)
        list = selector.xpath('//table[@class="exploit_list bootstrap-wrapper"]/tbody/tr')
        item = DownloadItem()
        for piece in list:
            dlink = piece.xpath('td[@class="dlink"]/a/@href').extract()  # dlink
            item['file_urls'] = dlink
            item['files'] = dlink[0].split("/")[4]
            yield item

        next = selector.xpath('//div[@class="pagination"]').re(r'href="(.*?)">next')
        if next:
            html_parser = HTMLParser.HTMLParser()
            url = html_parser.unescape(next[0])
            yield scrapy.http.Request(url, callback=self.parse)