from urllib.parse import urljoin

import scrapy
from scrapy.http import HtmlResponse


class DongmanSpider(scrapy.Spider):
    name = "dongman"
    allowed_domains = ["zol.com.cn"]
    start_urls = ["https://desk.zol.com.cn/dongman/"]

    def parse(self, response: HtmlResponse, **kwargs):
        photo_list = response.css(".photo-list-padding")
        for li in photo_list:
            link = li.css("a").attrib["href"]
            if link.endswith(".exe"):
                continue
            href = response.urljoin(link)
            yield scrapy.Request(href, self.obtain_img_detail)

        pages = response.css(".page a")
        for page in pages:
            page_url = response.urljoin(page.attrib["href"])
            yield scrapy.Request(page_url, self.parse)

    def obtain_img_detail(self, response: HtmlResponse):
        big_img = response.css("#bigImg").attrib["src"]
        yield {"big_img": big_img}
