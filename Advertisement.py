from bs4 import BeautifulSoup as bs
import requests


class Advertisement:
    def __init__(self):
        self.streets = []
        self.prices = []
        self.apartment_types = []
        self.cities = []
        self.areas = []
        self.secondary_areas = []
        self.scrape_yad2()

    def scrape_yad2(self):
        url = 'https://www.yad2.co.il/realestate/rent'
        try:
            r = requests.get(url, headers={'user-agent': 'Mozilla/7.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
            soup = bs(r.content)
            all_advertisements = soup.find_all("div", {'class': 'feeditem table'})
            for data in all_advertisements:
                self.prices.append(str(data.find("div", {'class': 'price'}).contents[0]).replace("\n", "").replace(" ", ""))
                self.streets.append(str(data.find("span", {'class': 'title'}).contents[0]).replace("\n", "").replace(" ", ""))
                apartment_info = str(data.find("span", {'class': 'subtitle'}).contents[0]).split(",")
                if len(apartment_info) == 4:
                    self.apartment_types.append(str(apartment_info[0]))
                    self.areas.append(str(apartment_info[1]))
                    self.secondary_areas.append(str(apartment_info[2]))
                    self.cities.append(str(apartment_info[3]))
                    continue

                self.apartment_types.append(str(apartment_info[0]))
                self.areas.append(str(apartment_info[1]))

                if len(apartment_info) > 2:
                    self.cities.append(str(apartment_info[2]))
        except Exception as e:
            print('error is: %s' % e)
