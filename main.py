from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"
url = "https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/results/?cycle=2014&ident="
errormsg = "Something Went Wrong!"
noLoop = False


def getout():
    pass


def get(furl):
    global links, driver

    try:
        driver = webdriver.Chrome(PATH)
    except:
        print("CD1")
        getout()

    else:
        driver.get(furl)

        try:
            print(driver.title)

        except:
            print("cd2")
            getout()

        else:

            try:
                links = driver.find_elements_by_xpath("//table[@id = 'resultsTable']//tbody/tr/td/a")

                a = []
                b = []
                for element in links:
                    a.append(element.text)
                    b.append(element.get_attribute("href"))

                for oa in a:
                    for ob in b:
                        print(oa + "\t" + ob)
                        break

            except NoSuchElementException:
                print("Selenium: No such element.")
            finally: driver.quit()




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
            get(furl)


if not noLoop:
    enter()
else:
    exit()
