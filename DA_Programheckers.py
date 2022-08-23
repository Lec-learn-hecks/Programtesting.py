#get recon,task 5
import requests
url = 'http://172.18.58.80/varsity/'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *", r.status_code)
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {'User-Agent' : 'Mobile'}
url2 = 'http://172.18.58.80/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)

#scrapy mapping,task 6
import scrapy
class NewSpider(scrapy.Spider):
 name = "new_spider"
 start_urls = ['http://172.18.58.80/varsity/']
 def parse(self, response):
               css_selector = 'img'
               for x in response.css(css_selector):
                  newsel = '@src'
                  yield {'Image Link': x.xpath(newsel).extract_first(),}

               #recurse next page,task 7
               Page_selector = '.next a ::attr(href)'
               next_page = response.css(Page_selector).extract_first()
               if next_page:
                   yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
                
 #unittest test
class SimpleTest(unittest.TestCase):

    def test_51(self):
        print(r.text)

    def test_52(self):
        self.assertEqual(r.status_code, 200)

    def test_53(self):
        print(h.headers[x])

    def test_54(self):
        self.assertEqual(rh.text, 'User Agent : Mobile')

    def test_6(self):
            yield {'Image Link': x.xpath(newsel).extract_first(), }

    def test_7(self):
        next_page = response.css(Page_selector).extract_first()
        if next_page:
          yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

if __name__ == '__main__':
    unittest.main()
