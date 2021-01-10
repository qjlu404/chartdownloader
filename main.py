from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
url = "https://airnav.com/airport/"

noloop = False


def get(furl):
    driver = webdriver.Chrome(PATH)
    driver.get(furl)
    print(driver.title)
    try:
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "PDF"))
        )
    except NoSuchElementException:
        print("ERROR: CD1")
        driver.quit()
        exit()
    finally:
        driver.quit()

    print(links.text)
    #for items in links:
    #    sleep(10)
    #    print(items)


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


if not noloop:
    enter()
else:
    exit()
