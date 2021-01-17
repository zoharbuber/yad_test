from scraper import Scraper
from advertisement_dao import AdvertisementDAO


if __name__ == '__main__':
    scraper = Scraper()
    advertisements = scraper.scrape_yad2()
    advertisement_dao = AdvertisementDAO()
    advertisement_dao.insert_advertisements(advertisements)
