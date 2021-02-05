if __name__ == '__main__':
    print('must run main.py first')
    exit(1)

from pdf2image import convert_from_path
from urllib.request import urlopen
from urllib.request import urlretrieve as download
from lxml import etree
import os


url = 'https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident='


def path(icao, type):
    if type == 'APP':
        finalpath = icao + "/Approach Plates"
    elif type == 'DEP':
        finalpath = icao + "/SIDS"
    elif type == 'ARR':
        finalpath = icao + "/STARS"
    else:
        finalpath = icao + "/Information"

    return finalpath


# Downloads the file using the given information
def dload(name, link, type, icao, choice):
    if choice == 1:
        ffile = type + "." + name.replace("/", "-")
        print(path(icao, type) + "/" + name.replace("/", "-") + ".pdf")
        print("8===>" + ffile)
        if not os.path.isdir("./" + path(icao, type)):
            os.makedirs("./" + path(icao, type))

        download(link, path(icao, type) + "/" + name.replace("/", "-") + ".pdf")

        if os.name == 'nt':
            images = convert_from_path(path(icao, type) + "/" + name.replace("/", "-") + ".pdf", poppler_path=r"./poppler-21.01.0/Library/bin")
            i = 1
            for img in images:

                if i != 1:
                    img.save(icao + "/" + icao + '/' + ffile + ' (PG-' + str(i) + ").png", 'PNG')
                else:
                    img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')
                i += 1

        else:
            images = convert_from_path(path(icao, type) + "/" + name.replace("/", "-") + ".pdf")
            i = 1
            for img in images:

                if i != 1:
                    img.save(icao + "/" + icao + '/' + ffile + 'PG-' + str(i) + ".png", 'PNG')
                else:
                    img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')
                i += 1

    if choice == 2:
        ffile = name.replace("/", "-")
        fpath = "./" + path(icao, type) + "/" + name.replace("/", "-") + ".pdf"
        print("8===>" + ffile)
        print(fpath)
        if not os.path.isdir("./" + path(icao, type)):
            os.makedirs("./" + path(icao, type))
        download(link, fpath)


# Gets website info and puts everything in the right format so it can be used by the dload function
def getdata(furl, icao, choice):
    def sendtodownload(anames, alinks, atypes, aicao, achoice):
        for i, j, k in zip(anames, alinks, atypes):
            if not os.path.exists(aicao + "/" + path(aicao, k)):
                os.makedirs(aicao + "/" + path(aicao, k))
            dload(i.replace(".", " "), j, k, aicao, achoice)

    response = urlopen(furl)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    infohtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[last()-2]")
    nameshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[8]/a")
    linkshtml = tree.xpath("//*[@id='resultsTable']/tbody/tr/td[8]/a/@href")
    names = []
    links = []
    types = []

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

    if choice == 1:
        if not os.path.exists(icao + "/" + icao):
            os.makedirs(icao + "/" + icao)

    sendtodownload(names, links, types, icao, choice)


# changes the url as needed.
def enter(icao, page, choice):
    print(icao)
    furl = url + icao + "&page=" + str(page)
    getdata(furl, icao.upper(), choice)
