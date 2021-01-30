if __name__ == '__main__':
    print('must run main.py first')
    exit(1)

from pdf2image import convert_from_path
from urllib.request import urlopen
from lxml import etree
import wget
import os


url = 'https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident='


def dload(name, link, type, icao, choice):

    if choice == 1:
        ffile = type + "." + name.replace("/", "-")
        print("    " + ffile)
        wget.download(link, icao + "/" + ffile + ".pdf")
        if os.name == 'nt':
            images = convert_from_path(icao + "/" + ffile + ".pdf", poppler_path=r"./poppler-21.01.0/Library/bin")
            for img in images:
                img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')
        else:
            images = convert_from_path(icao + "/" + ffile + ".pdf")
            print("    " + ffile)

            for img in images:
                img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')

    if choice == 2:
        ffile = name.replace("/", "-")
        wget.download(link, './' + icao + "/" + ffile + ".pdf")


def getdata(furl, icao, choice):
    response = urlopen(furl)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    infohtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[last()-2]")
    nameshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[8]/a")
    linkshtml = tree.xpath("//*[@id='resultsTable']/tbody/tr/td[8]/a/@href")
    names = []
    links = []
    types = []
    if choice == 1:
        if not os.path.exists(icao + "/" + icao):
            os.makedirs(icao + "/" + icao)

    for name in nameshtml:
        names.append(name.text)

    for link in linkshtml:
        links.append(link)

    for info in infohtml:
        if info.text == 'IAP':
            types.append('APP')

        elif info.text == 'DP':
            types.append('DEP')

        elif info.text == 'STAR':
            types.append('ARR')

        else:
            types.append('INF')

    for i, j, k in zip(names, links, types):
        dload(i.replace(".", " "), j, k, icao.upper(), choice)


def enter(icao, page, choice):
    print(icao)
    furl = url + icao + "&page=" + str(page)
    if not os.path.exists(icao.upper()):
        os.makedirs(icao.upper())
    getdata(furl, icao.upper(), choice)
