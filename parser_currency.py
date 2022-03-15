import requests
from bs4 import BeautifulSoup
import time
import smtplib


class Currency:
    EURO_RUB = "https://www.google.com/search?q=rehc+tdhj&oq"
    DOLLAR_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0"
    LIRA_RUB = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B8%D1%80%D1%8B"
    Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                             "99.0.4844.51 Safari/537.36"}

    current_convert_price_euro = 0
    difference_euro = 5

    current_convert_price_dollar = 0
    difference_dollar = 3

    current_convert_price_lira = 0
    difference_lira = 0.5

    def __init__(self):
        self.current_convert_price_euro = float(self.get_currency_price_euro().replace(",", "."))
        self.current_convert_price_dollar = float(self.get_currency_price_dollar().replace(",", "."))
        self.current_convert_price_lira = float(self.get_currency_price_lira().replace(",", "."))

    def get_currency_price_euro(self):
        full_page = requests.get(self.EURO_RUB, headers=self.Headers)

        soup = BeautifulSoup(full_page.content, "html.parser")

        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

        return convert[0].text

    def check_currency_euro(self):
        currency = float(self.get_currency_price_euro().replace(",", "."))
        if currency >= self.current_convert_price_euro + self.difference_euro:
            print(f"Курс евро вырос более чем на {self.difference_euro} рублей")
            self.current_convert_price_euro = currency
            self.send_mail("Euro")

        elif currency <= self.current_convert_price_euro - self.difference_euro:
            print(f"Курс евро упал более чем на {self.difference_euro} рублей")
            self.current_convert_price_euro = currency
            self.send_mail("Euro")

        print("Cейчас курс: 1 Евро = " + str(currency))
        time.sleep(3)

    def get_currency_price_dollar(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.Headers)

        soup = BeautifulSoup(full_page.content, "html.parser")

        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

        return convert[0].text

    def check_currency_dollar(self):
        currency = float(self.get_currency_price_dollar().replace(",", "."))
        if currency >= self.current_convert_price_dollar + self.difference_dollar:
            print(f"Курс доллара вырос более чем на {self.difference_dollar} рублей")
            self.send_mail("Dollar")

        elif currency <= self.current_convert_price_dollar - self.difference_dollar:
            print(f"Курс доллара упал более чем на {self.difference_dollar} рублей")
            self.send_mail("Dollar")

        print("Cейчас курс: 1 Доллар = " + str(currency))
        time.sleep(3)

    def get_currency_price_lira(self):
        full_page = requests.get(self.LIRA_RUB, headers=self.Headers)

        soup = BeautifulSoup(full_page.content, "html.parser")

        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

        return convert[0].text

    def check_currency_lira(self):
        currency = float(self.get_currency_price_lira().replace(",", "."))
        if currency >= self.current_convert_price_lira + self.difference_lira:
            print(f"Курс Турецкой лиры вырос более чем на {self.difference_lira} рублей")
            self.send_mail("Turkish Lira")

        elif currency <= self.current_convert_price_lira - self.difference_lira:
            print(f"Курс Турецкой лиры упал более чем на {self.difference_lira} рублей")
            self.send_mail("Turkish Lira")

        print("Cейчас курс: 1 Турецкая Лира = " + str(currency))
        time.sleep(3)

    @staticmethod
    def send_mail(arg: str):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("aleksandr.ulitin14@gmail.com", "bkumlmuzixlfqxbt")

        subject = f"The currency {arg}"
        body = f"course {arg} has changed"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            "aleksandr.ulitin14@gmail.com",
            "aleksandr.ulitin14@gmail.com",
            message
        )
        server.quit()


while True:
    cur = Currency()
    cur.check_currency_euro()
    cur.check_currency_dollar()
    cur.check_currency_lira()
    print("-------------------------------------")
    continue
