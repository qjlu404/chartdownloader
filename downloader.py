if __name__ == '__main__':
    print('must run main.py first')
    exit(1)

from pdf2image import convert_from_path
from urllib.request import urlopen
from urllib.request import urlretrieve as download
import threading
from lxml import etree
import os
import config

URL = 'https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=' + str(config.chartVersion) + '&ident='


def path(icao, typee):
    if typee == 'APP':
        finalpath = icao + "/Instrument Approaches"
    elif typee == 'DEP':
        finalpath = icao + "/SIDS"
    elif typee == 'ARR':
        finalpath = icao + "/STARS"
    else:
        finalpath = icao + "/Information"

    return finalpath


# Downloads the file using the given information
def dload(name, link, typeinfo, icao, choice):
    if choice == 1:
        ffile = typeinfo + "." + name.replace("/", "-")
        try:
            if not os.path.isdir(path(icao, typeinfo)):
                os.makedirs(path(icao, typeinfo))
        except FileExistsError:
            if not os.path.isdir(path(icao, typeinfo)):
                os.makedirs(path(icao, typeinfo))

        download(link, path(icao, typeinfo) + "/" + name.replace("/", "-") + ".pdf")
        if os.name == 'nt':
            images = convert_from_path(path(icao, typeinfo) + "/" + name.replace("/", "-") + ".pdf", poppler_path=r"./poppler-21.01.0/Library/bin")
            i = 1
            for img in images:

                if i != 1:
                    img.save(icao + "/" + icao + '/' + ffile + ' (PG-' + str(i) + ").png", 'PNG')
                else:
                    img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')
                i += 1

        else:
            images = convert_from_path(path(icao, typeinfo) + "/" + name.replace("/", "-") + ".pdf")
            i = 1
            for img in images:

                if i != 1:
                    img.save(icao + "/" + icao + '/' + ffile + ' (PG-' + str(i) + ").png", 'PNG')
                else:
                    img.save(icao + "/" + icao + '/' + ffile + ".png", 'PNG')
                i += 1

        print("8===>" + ffile)

    if choice == 2:
        ffile = name.replace("/", "-")
        fpath = "./" + path(icao, typeinfo) + "/" + name.replace("/", "-") + ".pdf"
        try:
            if not os.path.isdir(path(icao, typeinfo)):
                os.makedirs(path(icao, typeinfo))
        except FileExistsError:
            if not os.path.isdir(path(icao, typeinfo)):
                os.makedirs(path(icao, typeinfo))
        download(link, fpath)
        print("8===>" + ffile)


# Gets website info and puts everything in the right format so it can be used by the dload function
def getdata(furl, icao, choice):
    threads = []

    def dlloop(anames, alinks, atypes, aicao, achoice):
        for i, j, k in zip(anames, alinks, atypes):
            if not os.path.exists(aicao + "/" + path(aicao, k)):
                os.makedirs(aicao + "/" + path(aicao, k))
            th = threading.Thread(target=dload, args=(i.replace(".", " "), j, k, aicao, achoice))
            th.start()
            threads.append(th)
        for thread in threads:
            thread.join()

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

    dlloop(names, links, types, icao, choice)


# changes the url as needed.
def enter(icao, page, choice):
    print(icao)
    furl = URL + icao + "&page=" + str(page)
    getdata(furl, icao.upper(), choice)
