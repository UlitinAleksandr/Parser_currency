import requests
from bs4 import BeautifulSoup
import time


DOLLAR_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=" \
                 "%D0%BA%D1%83%D1%80%D1%81+&aqs=chrome.0.69i59l3j35i39j69i57j69i61l3.1027j1j9&sourceid=chrome&ie=UTF-8"
EURO_RUB = "https://www.google.com/search?q=rehc+tdhj&oq=rehc+tdhj&aqs=chrome" \
               "..69i57j0i10i131i395i433l4j0i10i131i433j0i10j0i10i433j0i10j0i10i131i433.1277j1j7&sourceid=chrome&i" \
           "e=UTF-8"
LIRA_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D1%8B+%D0%BA+%D1%" \
               "80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%" \
               "80%D1%8B&aqs=chrome.0.69i59j69i57j0i512j0i20i263i512j0i512l6.3138j1j9&sourceid=chrome&ie=UTF-8"
Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                         "99.0.4844.51 Safari/537.36"}


def check_currency_euro():

    full_page = requests.get(EURO_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})
    print("Cейчас курс: 1 Евро = " + convert[0].text)
    time.sleep(3)


def check_currency_dollar():
    full_page = requests.get(DOLLAR_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    print("Cейчас курс: 1 Доллар = " + convert[0].text)
    time.sleep(3)


def check_currency_lira():
    full_page = requests.get(LIRA_RUB, headers=Headers)

    soup = BeautifulSoup(full_page.content, "html.parser")

    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

    print("Cейчас курс: 1 Лира = " + convert[0].text)
    time.sleep(3)


if __name__ == '__main__':
    check_currency_euro()
    check_currency_dollar()
    check_currency_lira()