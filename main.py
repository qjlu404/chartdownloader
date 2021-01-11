from urllib.request import urlopen
from lxml import etree
url = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident="
errormsg = "Something Went Wrong!"
noLoop = False


def downloadChart(name, site):
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
        print(name.text)
        names.append(name.text)
    for link in linkshtml:
        print(link)
        links.append(link)

    print("\n\n\n\n", names[2])
    print(links[2])

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
