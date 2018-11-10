# ; G3O IP
# ; Created By: Ob1t0
# ; Version: 1.0
# ; Require: BeautifulSoup4, Requests

class GeoIP_:
    # Testando as bibliotecas | Testing the modules
    try:
        from urllib.request import urlopen
        from bs4 import BeautifulSoup as bs
        from os import sys
    except:
        print("[ERROR] You need install BeautifulSoup4 lib, Urllib and Html5lib to continue...")

    # Pegando as informações | Gethering Informations
    host = urlopen("https://iplocation.com/")
    raw = bs(host.read(), "html5lib")
    ip = raw.findAll("b", {"class":"ip"})
    lat = raw.findAll("td", {"class":"lat"})
    lng = raw.findAll("td", {"class":"lng"})
    country = raw.findAll("span", {"class":"country_name"})
    region = raw.findAll("span", {"class":"region_name"})
    company = raw.findAll("td", {"class":"company"})

    for ip_f in ip:
        ip_f = ip_f.getText()
        print("---=[ I N F O R M A T I O N S ]=---")
        print("+ Internet Protocol :", ip_f)
        for country_f in country:
            country_f = country_f.getText()
            print("+ Country           :", country_f)
        for region_f in region:
            region_f = region_f.getText()
            print("+ Region            :", region_f)
        for company_f in company:
            company_f = company_f.getText()
            print("+ Company           :", company_f)
        for lat_f in lat:
            lat_f = lat_f.getText()
            print("+ Latitude          :", lat_f)
        for lng_f in lng:
            lng_f = lng_f.getText()
            print("+ Longitude         :", lng_f)
            print("---=[ I N F O R M A T I O N S ]=---")
if __name__ == "__main__":
    GeoIP_()
