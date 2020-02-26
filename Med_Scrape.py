import requests
import random
import re
from bs4 import BeautifulSoup
import urllib.request

# measurement = ["cup", "cups", "tablespoon", "tablespoons", "teaspoon", "teaspoons", "spoon", "cloves", "jars", "pound",
#                "pinch", "links", "link"]


class OTC_Search:
    search_base_url = "http://search.jsm-db.info/sp_en/result.php?search=%s"
    image_url="http://search.jsm-db.info/sp_en/"


    def search_medicines(self, keywords):
        search_url = self.search_base_url % (keywords.replace(' ', '+'))
        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content)
        for i in page_graph.find_all('p', {'class', "name"}):
            # print("Nutrients")
            print(i.text)
        for i in page_graph.find_all('p', {'class', "summary"}):
            # print("Nutrients")
            print(i.text)
        for i in page_graph.find_all('p', {'class', "price"}):
            # print("Nutrients")
            print(i.text)
        for i in page_graph.find_all('div', {'class', "img_wrap"}):
            # print("Nutrients")
            pattern = re.compile(r'(<img src=)(\")(.*)\"')
            nutr_link_url = pattern.search(str(i.img)).group(3)
            print(nutr_link_url)
            print(i.img)
        # print(page_graph)

    def download_image(url):
        print("[INFO] downloading {}".format(url))
        name = random.randrange(1, 100)
        fullname = str(name) + ".jpg"
        name = str(url.split('/')[-1])
        urllib.request.urlretrieve(url, fullname)

med = OTC_Search()
print("Enter medicine detail")
inp=input()
med = med.search_medicines(inp)
print(med)
# results = rf.scrape_recipe(meat_lasagna)

# import fractions
# fraction_str = "1 1/2"
# fraction_obj = sum(map(fractions.Fraction, fraction_str.split()))
# print(float(fraction_obj))
# fractions.Fraction.from_float(float(fraction_obj)/2).limit_denominator()
