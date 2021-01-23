from pdf2image import convert_from_path
from urllib.request import urlopen
from lxml import etree
import wget
import os


url = 'https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident='
noLoop = False


def dload(name, link, type, icao, choice):
    if choice.lower() == 'n':
        ffile = name.replace("/", "-")
        wget.download(link, './' + icao + "/" + ffile + ".pdf")
        print(ffile)

    else:
        ffile = type + "." + name.replace("/", "-")
        wget.download(link, icao + "/" + ffile + ".pdf")
        images = convert_from_path(icao + "/" + ffile + ".pdf")
        for img in images:
            img.save(icao + "-png/" + ffile + ".png", 'PNG')
        print(ffile)


def getdata(furl, icao, choice):
    response = urlopen(furl)
    print(".")
    htmlparser = etree.HTMLParser()
    print(".")
    tree = etree.parse(response, htmlparser)
    print(".")
    infohtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[last()-2]")
    nameshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a")
    linkshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a/@href")
    print(".")

    names = []
    links = []
    types = []
    print(".")
    if choice.lower() == 'y':

        if not os.path.exists("./" + icao.upper() + "-png/"):
            os.makedirs("./" + icao.upper() + "-png/")
    print(".")
    for name in nameshtml:
        names.append(name.text)
    print(".")
    for link in linkshtml:
        links.append(link)
    print(".")
    for info in infohtml:
        if info.text == 'IAP':
            types.append('APP')

        elif info.text == 'DP':
            types.append('DEP')

        elif info.text == 'STAR':
            types.append('ARR')

        else:
            types.append('INF')
    print(".")
    for i, j, k in zip(names, links, types):
        dload(i.replace(".", "_"), j, k, icao.upper(), choice)


def enter(icao, page, choice):
    furl = url + icao + "&page=" + page
    loop = False
    path = icao.upper()
    if not os.path.exists(path):
        os.makedirs(path)
    getdata(furl, icao, choice)