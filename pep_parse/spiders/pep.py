import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ["peps.python.org"]
    start_urls = [f'https://{url}' for url in allowed_domains]

    def parse(self, response):
        for link in response.css(
            '#numerical-index table.pep-zero-table tbody tr a::attr(href)'
        ):
            yield response.follow(link.get(), callback=self.parse_pep)

    def parse_pep(self, response):
        info = response.css('h1.page-title::text').get().split()
        yield PepParseItem(
            number=info[1],
            name="".join(info[3:]),
            status=response.css('dt:contains("Status")+dd abbr::text').get(),
        )
