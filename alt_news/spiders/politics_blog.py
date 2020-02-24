# -*- coding: utf-8 -*-
import scrapy


class PoliticsBlogSpider(scrapy.Spider):
    name = 'politics-blog'
    allowed_domains = ['www.altnews.in/topics/politics/']
    start_urls = ['https://www.altnews.in/topics/politics/']
    custom_settings = {
        "FEED_URI": "tmp/cat-politics.csv"
    }

    autothrottle_enabled = True
    def parse(self, response):
        for blog in response.css("article.herald-lay-b"):
            yield {
                "title" : blog.css(".entry-title a::text").get(),
                "link" :  blog.css(".entry-title a::attr(href)").get(),
                "author" : blog.css(".author a::text").get(),
                "short_des" : blog.css(".entry-content p::text").get(),
                'date' : blog.css(".herald-date span.updated::text").get(),
                "img" : blog.css(".herald-post-thumbnail img::attr(src)").get(),
            }


        # next_page = response.css(".herald-main-content .herald-pagination  a.next::attr(href) ").extract()
        # if next_page is not None:
        #     next_page = response.urlJoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        next_page = response.css('.herald-pagination a.next::attr(href)').get()
        if next_page is not None:
            # yield response.follow(next_page, callback=self.parse)
            scrapy.Request(response.urljoin(next_page))
