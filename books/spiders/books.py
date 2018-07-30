import scrapy
import math

class Iphone8_64Spider(scrapy.Spider):
    name = "iphone8_64"
    start_urls = [
        'https://www.belsimpel.nl/apple-iphone-8/64gb-zwart/aanbieding?abonnement=t-mobile-normaal-go-next-2-jaar-hsnwa',
        'https://www.belsimpel.nl/apple-iphone-8/64gb-zwart/aanbieding?abonnement=t2-0-minuten-5000-mb-4g-2-jaar',
        'https://www.belsimpel.nl/apple-iphone-8/64gb-zwart/aanbieding?abonnement=vodafone-red-2-jaar',
        'https://www.mobiel.nl/abonnement/t-mobile/t-mobile-go-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31300&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31234&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/vodafone/vodafone-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31635&%5Bmax_price_incl_btw%5D=0#',
    ]
    def parse(self, response):
        if 'belsimpel.nl' in response.request.url:
            for item in response.css('div.pd_chosen_offer_cta'):
                    yield {
                        'url': response.request.url,
                        'prijs': float(item.xpath('//*[@class="pd_offer_picker_row pd_offer_picker_row_hardware_cost"]/*/text()').extract_first().strip()[2:-2].replace(',','')),
                        'abo': 'FUTURE',
                        'provider': item.xpath('//*[@class="pd_offer_picker_product_images_provider"]/*/@alt').extract_first()[:-11],
                        'toestel': 'iphone8_64',
                        'shop': 'belsimpel'
                    }
        else:
            for item in response.xpath('//*[@class="proposed-phone__row js-phone-proposition"]'):
                try:
                    if 'iphone 8 64' in item.css('div.proposed-phone__image-and-name::text').extract()[1].strip().lower():
                        yield {
                            'url': response.request.url,
                            'prijs': float(item.css('span.proposed-phone__monthly-price::text').extract_first().strip()[2:4]),
                            'abo': 'FUTURE',
                            'provider': response.request.url.split("/")[4],
                            'toestel': 'iphone8_64',
                            'shop': 'mobiel'
                        }
                except:
                    continue
