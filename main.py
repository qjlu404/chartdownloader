from pdf2image import convert_from_path
from urllib.request import urlopen
from lxml import etree
from time import sleep
import wget
import os
url = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident="
noLoop = False



def dload(name, link, type, icao, choice):
    global ffile
    name.replace("A/FD", "A-FD")
    print(name)
    if choice.upper() == 'N':
        ffile = name.replace("A/FD", "A-FD")
        wget.download(link, './' + icao + "/" + ffile + ".pdf" )
        
    else:
        ffile = type + "." + name.replace("A/FD", "A-FD")
        wget.download(link, './' + icao + "/" + ffile + ".pdf" )
        images = convert_from_path('./' + icao + "/" + ffile + ".pdf")
        for img in images:
            img.save(ffile, 'PNG')
    
    

    print(ffile)
    

def getdata(furl, icao):
    response = urlopen(furl)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    infohtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td[last()-2]")
    nameshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a")
    linkshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a/@href")

    names = []
    links = []
    types = []
    choice = input('Save for Aerobask planes?(y/n): ')

    for name in nameshtml:
        names.append(name.text)

    for link in linkshtml:
        links.append(link)

    for info in infohtml:
        if info.text == 'IAP':
            types.append('APP')

        elif info.text == 'DP':
            types.append('DPP')

        elif info.text == 'STAR':
            types.append('ARR')

        else:
            types.append('INF')

    for i, j, k in zip(names, links, types):
        i.replace("/", "-")
        dload(i, j, k, icao, choice)


def enter():
    loop = True
    while loop:
        global icao
        icao = input("Enter ICAO: ")
        page = input("Enter page number (faa website has multiple pages for data so just choose 1 then next time choose 2 for the next set of data): ")

        if len(icao) == 0:
            print("Please enter an ICAO")

        elif page == 0 or len(page) == 0:
            print("Please enter a page number from 1 and up until you get no more charts.")

        elif len(icao) > 4 or len(icao) < 4:
            print("ICAO must be 4 characters\n")

        else:
            furl = url + icao + "&page=" + page
            loop = False
            path = icao.lower()
            if not os.path.exists(path):
                os.makedirs(path)
            getdata(furl, icao)


if not noLoop:
    enter()
else:
    exit()
