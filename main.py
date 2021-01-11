from urllib.request import urlopen
from lxml import etree
url = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident="
errormsg = "Something Went Wrong!"
noLoop = False


def downloadchart(name, site):
    pass


def getdata(furl):
    response = urlopen(furl)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    nameshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a")
    linkshtml = tree.xpath("//table[@id='resultsTable']/tbody/tr/td/a/@href")
    names = []
    links = []

    for name in nameshtml:
        names.append(name.text)
    for link in linkshtml:
        links.append(link)
    items = dict(zip(names, links))

    for item in items:
        print(item, '->', items[item])


def enter():
    loop = True
    while loop:
        icao = input("Enter ICAO: ")

        if len(icao) == 0:
            print("Please enter an ICAO")

        elif len(icao) > 4 or len(icao) < 4:
            print("ICAO must be 4 characters\n")

        else:
            furl = url + icao
            loop = False
            getdata(furl)


if not noLoop:
    enter()
else:
    exit()
