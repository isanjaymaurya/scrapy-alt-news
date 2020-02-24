from scrapy import cmdline
cmdline.execute("scrapy crawl politics-blog".split())
# cmdline.execute("scrapy list|xargs -n 1 scrapy crawl")