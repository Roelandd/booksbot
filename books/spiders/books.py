import scrapy
import math

class BelsimpelSpider(scrapy.Spider):

    name = "belsimpelspider"
    devices = [
        'samsung-galaxy-s8/zwart/',
        'samsung-galaxy-s9/zwart/',
        'samsung-galaxy-s9-plus/64gb-zwart',
        'apple-iphone-x/64gb-zwart/',
        'apple-iphone-8/64gb-zwart/',
        'apple-iphone-8-plus/64gb-zwart/',
        'apple-iphone-7/32gb-zwart/'
        'oneplus-6/zwart/',
        'huawei-p20-lite/zwart/',
        'huawei-p20/zwart/',
        'huawei-p20-pro/zwart/'
    ]
    subscriptions = [
        't-mobile-normaal-go-next-2-jaar-hsnwa3',
        't-mobile-normaal-go-next-2-jaar-hsnwa',
        'vodafone-red-2-jaar',
        'vodafone-red-iphonex-2-jaar',
        'vodafone-start-xl-2-jaar',
        't2-100-minuten-2000-mb-4g-2-jaar',
        't2-100-minuten-5000-mb-4g-2-jaar',
        't2-100-minuten-10000-mb-4g-2-jaar',
        't2-onbeperkt-bellen-onbeperkt-mb-4g-2-jaar',
        'hollandsnieuwe-6000-mb-min-sms-4g-2-jaar',
        'telfortnieuw-150-minuten-10000-mb-4g-2-jaar',
        'kpn-basis-2-jaar',
        'kpn-zorgeloos-standaard-2-jaar'
    ]
    start_urls = []

    for dev in devices:
        for sub in subscriptions:
            url = 'http://www.belsimpel.nl/' + dev + 'aanbieding?abonnement=' + sub
            start_urls.append(url)

    def get_subscription(self,url):
    	if 't-mobile-normaal-go-next-2-jaar-hsnwa' in url:
    		return 'go next'
    	elif 'vodafone-red-2-jaar' in url:
    		return 'red'
    	elif 'vodafone-start-xl-2-jaar' in url:
    		return 'start xl'
    	elif 't2-100-minuten-2000-mb-4g-2-jaar' in url:
    		return '100/2000'
    	elif 't2-100-minuten-5000-mb-4g-2-jaar' in url:
    		return '100/5000'
    	elif 't2-100-minuten-10000-mb-4g-2-jaar' in url:
    		return '100/10000'
    	elif 't2-onbeperkt-bellen-onbeperkt-mb-4g-2-jaar' in url:
    		return 'onbeperkt'
    	elif 'hollandsnieuwe-6000-mb-min-sms-4g-2-jaar' in url:
    		return '6000 min/sms/mb'
    	elif 'telfortnieuw-150-minuten-10000-mb-4g-2-jaar' in url:
    		return '150/10000'
    	elif 'kpn-basis-2-jaar' in url:
    		return 'basis'
    	elif 'kpn-zorgeloos-standaard-2-jaar' in url:
    		return 'zorgeloos standaard'

    def parse(self, response):
        for item in response.css('div.pd_chosen_offer_cta'):
            yield {
                'url': response.request.url,
                'prijs': float(item.xpath('//*[@class="pd_offer_picker_row pd_offer_picker_row_hardware_cost"]/*/text()').extract_first().strip()[2:-2].replace(',',''))/24,
                'abo': self.get_subscription(response.request.url),
                'provider': item.xpath('//*[@class="pd_offer_picker_product_images_provider"]/*/@alt').extract_first()[:-11].lower(),
                'toestel': item.xpath('//*[@id="pd_title"]/text()').extract_first().strip(),
                'shop': 'belsimpel'
            }



class MobielSpider(scrapy.Spider):
    name = "mobielspider"
    start_urls = [
        'https://www.mobiel.nl/abonnement/t-mobile/t-mobile-go-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31300&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/vodafone/vodafone-start-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=32154&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/vodafone/vodafone-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31635&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31233&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31234&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31235&%5Bvoice_bundle%5D=31237&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/tele2/tele2-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=31236&%5Bvoice_bundle%5D=31238&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/hollandsnieuwe/hollandsnieuwe-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=36026&%5Bvoice_bundle%5D=36290&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/telfort/telfort-mobiel-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=35678&%5Bvoice_bundle%5D=35680&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-basis-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30871&%5Bmax_price_incl_btw%5D=0#',
        'https://www.mobiel.nl/abonnement/kpn/kpn-zorgeloos-2-jaar?utf8=%E2%9C%93&%5Bmain_bundle%5D=30979&%5Bmax_price_incl_btw%5D=0#'
    ] 

    def get_subscription(self,url):
    	if 't-mobile-go' in url:
    		return 'go next'
    	elif 'vodafone-2-jaar' in url:
    		return 'red'
    	elif 'vodafone-start-2-jaar' in url:
    		return 'start xl'
    	elif '31233' in url:
    		return '100/2000'
    	elif '31234' in url:
    		return '100/5000'
    	elif '31235' in url:
    		return '100/10000'
    	elif '31236' in url:
    		return 'onbeperkt'
    	elif 'hollandsnieuwe' in url:
    		return '6000 min/sms/mb'
    	elif 'telfort' in url:
    		return '150/10000'
    	elif 'kpn-basis' in url:
    		return 'basis'
    	elif 'kpn-zorgeloos' in url:
    		return 'zorgeloos standaard'

    def parse(self, response):
        for item in response.xpath('//*[@class="proposed-phone__row js-phone-proposition"]'):
            try:
                yield {
                    'url': response.request.url,
#                   'prijs': float(item.css('span.proposed-phone__monthly-price::text').extract_first().strip()[2:4]),
					'prijs': item.css('dd.proposition__price-details__value').extract()[1],
                    'abo': self.get_subscription(response.request.url),
                    'provider': response.request.url.split("/")[4],
                    'toestel': item.css('div.proposed-phone__image-and-name::text').extract()[1].strip(),
                    'shop': 'mobiel'
                }
            except:
                continue
