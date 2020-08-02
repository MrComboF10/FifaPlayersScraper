import bs4
import requests
from selenium import webdriver

# chrome_driver = webdriver.Chrome("C:\\Users\\pcost\\chromedriver_win32\\chromedriver.exe")
# delay = 3  # delay to load page


# player_group -> "/top"
# filter_url -> "?league=13&order=desc"
# year -> 19
def scrap_page(year):
    page_url = "https://www.fifaindex.com/pt/players/fifa{}/".format(year)
    request_page = requests.get(page_url)
    soup = bs4.BeautifulSoup(request_page.content, "html.parser")
    # print(soup)
    scrap_dates_id(soup)


def scrap_dates_id(page_soup):
    dates_soup = []
    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for a in page_soup.findAll("a", class_="dropdown-item"):
        for month in months:
            if month in str(a):
                dates_soup.append(a)
                break

    for date in dates_soup:
        print(date)


scrap_page(19)
