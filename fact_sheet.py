import requests
import random
import re
from bs4 import BeautifulSoup
# import beautifulsoup4
import urllib.request
import json

# measurement = ["cup", "cups", "tablespoon", "tablespoons", "teaspoon", "teaspoons", "spoon", "cloves", "jars", "pound",
#                "pinch", "links", "link"]


class Embassy_Search:
    search_url = "https://www.usembassy.gov/japan/"
    image_url="http://search.jsm-db.info/sp_en/"

    def search_embassies(self, keywords):
        # search_url = self.search_base_url % (keywords.replace(' ', '+'))
        page_html = requests.get(self.search_url)
        page_graph = BeautifulSoup(page_html.content)
        # h=page_graph.find_all('p', {'class', "number"})
        # print("Total Results",h.number)
        embassies={}
        embassies[0]="" 
        #json_data = json.dumps()
        embassy_num = 0
        for i in page_graph.find_all('div', {'class', "cityname1"}):
            # json_data = json.dumps({'embassies'[embasy_num].'id': i.find('strong').text})
            embassies[embassy_num]= i.text 
            embassy_num+=1
            print (i)
            print(embassies)

        with open('embassies.json', 'w') as outfile:
            json.dump(embassies, outfile)
        
class Vaccine_Search:
    search_url = "https://wwwnc.cdc.gov/travel/destinations/traveler/none/japan"
    image_url="http://search.jsm-db.info/sp_en/"

    def search_vaccines(self, keywords):
        # search_url = self.search_base_url % (keywords.replace(' ', '+'))
        page_html = requests.get(self.search_url)
        page_graph = BeautifulSoup(page_html.content)
        # h=page_graph.find_all('p', {'class', "number"})
        # print("Total Results",h.number)
        vaccines=[]
        #json_data = json.dumps()
        for i in page_graph.find_all('td', {'class', "traveler-disease"}):
            # json_data = json.dumps({'embassies'[embasy_num].'id': i.find('strong').text})
            vaccines.append(i.text)
            print (i)
            print(vaccines)

        with open('vaccines.txt', 'w') as outfile:
            json.dump(vaccines, outfile)
       
    #     for i in page_graph.find_all('li', {'class', "item"}):
    #         for j in i.find_all('p', {'class', "name"}):
    #             print("inside",j.text)
    #         # print("Nutrients")
    #         for j in i.find_all('p', {'class', "summary"}):
    #             print("summ",j.text)
    #         for j in i.find_all('p', {'class', "maker"}):
    #             print("maker",j.text)
    #         for j in i.find_all('p', {'class', "amount"}):
    #             print("amount",j.text)
    #         for j in i.find_all('p', {'class', "price"}):
    #             print("price",j.text)
    #     # for i in page_graph.find_all('p', {'class', "price"}):
    #     #     # print("Nutrients")
    #     #     print(i.text)
    #     #     for j in i.find_all('p', {'class', "summary"}):
    #     #     # print("Nutrients")
    #     #         print("Summary",j.text)
    #     # for i in page_graph.find_all('p', {'class', "price"}):
    #     #     # print("Nutrients")
    #     #     print(i.text)
    #     for i in page_graph.find_all('div', {'class', "img_wrap"}):
    #         # print("Nutrients")
    #         pattern = re.compile(r'(<img src=)(\")(.*)\"')
    #         nutr_link_url = pattern.search(str(i.img)).group(3)
    #         print(nutr_link_url)
    #         print(i.img)
    #     # print(page_graph)
    #
    # def download_image(url):
    #     print("[INFO] downloading {}".format(url))
    #     name = random.randrange(1, 100)
    #     fullname = str(name) + ".jpg"
    #     name = str(url.split('/')[-1])
    #     urllib.request.urlretrieve(url, fullname)

med = Embassy_Search()
med2 = Vaccine_Search()
# print("Enter medicine detail")
# inp=input()
med.search_embassies("test")
med2.search_vaccines("test")
# results = rf.scrape_recipe(meat_lasagna)

# import fractions
# fraction_str = "1 1/2"
# fraction_obj = sum(map(fractions.Fraction, fraction_str.split()))
# print(float(fraction_obj))
# fractions.Fraction.from_float(float(fraction_obj)/2).limit_denominator()
