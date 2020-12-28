from bs4 import BeautifulSoup as bs
import requests
from Advertisement import Advertisement

class Scraper:

    def scrape_yad2(self):
        advertisemnets = []

        url = 'https://www.yad2.co.il/realestate/rent'
        try:
            r = requests.get(url, headers={'user-agent': 'Mozilla/1.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
            soup = bs(r.content)
            i = 2
            while soup.find_all("div", {'class': 'captcha-wrapper'}):
                r = requests.get(url, headers={'user-agent': 'Mozilla/"%s" (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' % i})
                soup = bs(r.content)
                i = i + 1

            all_advertisements = soup.find_all("div", {'class': 'feeditem table'})
            for data in all_advertisements:
                secondary_area = None
                city = None
                area = None

                tmp_price = str(data.find("div", {'class': 'price'}).contents[0]).replace("\n", "").replace(" ", "").replace("₪", "").replace(",", "")
                if tmp_price.isdigit():
                    price = int(tmp_price)
                street = str(data.find("span", {'class': 'title'}).contents[0]).replace("\n", "").replace(" ", "")
                apartment_info = str(data.find("span", {'class': 'subtitle'}).contents[0]).split(",")
                apartment_type = apartment_info[0]
                if len(apartment_info) >= 2:
                    area = apartment_info[1]

                if len(apartment_info) == 4:
                    secondary_area = apartment_info[2]
                    city = apartment_info[3]
                else:
                    if len(apartment_info) > 2:
                        city = apartment_info[2]

                advertisemnets.append(Advertisement(street, price, apartment_type, city, area, secondary_area))
            return advertisemnets

        except Exception as e:
            print('error is: %s' % e)
            raise
