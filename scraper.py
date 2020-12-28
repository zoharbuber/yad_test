 from bs4 import BeautifulSoup as bs
import requests
from Advertisement import Advertisement

class Scraper:

    def scrape_yad2(self):
        advertisemnets = []

        url = 'https://www.yad2.co.il/realestate/rent'
        try:
            r = requests.get(url, headers={
                'user-agent': 'Mozilla/13.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
            soup = bs(r.content)
            all_advertisements = soup.find_all("div", {'class': 'feeditem table'})
            for data in all_advertisements:
                secondary_area = None
                city = None
                area = None

                price = str(data.find("div", {'class': 'price'}).contents[0]).replace("\n", "").replace(" ", "")
                street = str(data.find("span", {'class': 'title'}).contents[0]).replace("\n", "").replace(" ", "")
                apartment_info = str(data.find("span", {'class': 'subtitle'}).contents[0]).split(",")
                apartment_type = apartment_info[0]
                if len(apartment_info) >= 2:
                    area = str(apartment_info[1])

                if len(apartment_info) == 4:
                    secondary_area = str(apartment_info[2])
                    city = str(apartment_info[3])
                else:
                    if len(apartment_info) > 2:
                        city = str(apartment_info[2])

                advertisemnets.append(Advertisement(street, price, apartment_type, city, area, secondary_area))
            return advertisemnets

        except Exception as e:
            print('error is: %s' % e)
            raise
