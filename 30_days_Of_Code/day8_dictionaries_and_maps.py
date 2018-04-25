"""
Title     : day8_dictionaries_and_maps
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
