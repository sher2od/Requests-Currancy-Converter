import json
import requests

# USD va EUR kurslarini olish uchun linklar
url_usd = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
url_eur = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'

print("1. USD → UZS")
print("2. UZS → USD")
print("3. EUR → UZS")
print("4. UZS → EUR")

choice = input("Tanlang >> ")

# USD → UZS
if choice == "1":
    amount = float(input("Dollar miqdori >> "))
    response = requests.get(url_usd)
    data = json.loads(response.content.decode())
    kurs = float(data[0]['Rate'])
    result = kurs * amount
    print(f"{amount} USD = {result:,.2f} UZS")

# UZS → USD
elif choice == "2":
    amount = float(input("UZS miqdori >> "))
    response = requests.get(url_usd)
    data = json.loads(response.content.decode())
    kurs = float(data[0]['Rate'])
    result = amount / kurs
    print(f"{amount} UZS = {result:,.2f} USD")

# EUR → UZS
elif choice == "3":
    amount = float(input("Yevro miqdori >> "))
    response = requests.get(url_eur)
    data = json.loads(response.content.decode())
    kurs = float(data[0]['Rate'])
    result = kurs * amount
    print(f"{amount} EUR = {result:,.2f} UZS")

# UZS → EUR
elif choice == "4":
    amount = float(input("UZS miqdori >> "))
    response = requests.get(url_eur)
    data = json.loads(response.content.decode())
    kurs = float(data[0]['Rate'])
    result = amount / kurs
    print(f"{amount} UZS = {result:,.2f} EUR")

else:
    print("Noto‘g‘ri tanlov!")
