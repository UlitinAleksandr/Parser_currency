import requests
from bs4 import BeautifulSoup
import time
import smtplib


class Currency:
    EURO_RUB = "https://www.google.com/search?q=rehc+tdhj&oq"
    Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"" Chrome/"
                             "99.0.4844.51 Safari/537.36"}

    current_convert_price = 0
    difference = 1

    def __init__(self):
        self.current_convert_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.Headers)

        soup = BeautifulSoup(full_page.content, "html.parser")

        convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})

        return convert[0].text

    def check_currency_euro(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_convert_price + self.difference:
            print("Курс вырос")
            self.send_mail()
        elif currency <= self.current_convert_price - self.difference:
            print("Курс упал")
            self.send_mail()
        print("Cейчас курс: 1 Евро = " + str(currency))
        time.sleep(3)
        self.check_currency_euro()

    def send_mail(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("aleksandr.ulitin14@gmail.com", "771307qqqqwE")

        subject = "Курс валют"
        body = "Курс изменился"
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            "sasha_parcer@gmail.com",
            "aleksandr.ulitin14@gmail.com",
            message
        )
        server.quit()


cur = Currency()
cur.check_currency_euro()
