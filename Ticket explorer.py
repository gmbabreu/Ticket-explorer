from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Define Departing Airport code
AIRPORT = ""

#Define Budget
BUDGET = ""

# Add any cities you want to be excluded
scratch_locations = []




def explore():
    """Function for navigating all the websites"""
    with open('Ticket_explorer.txt', 'w') as f:
        # iterate through destinations 
        f.write("Cheapest destinations under "+BUDGET+"\n\n")

        f.write("-------------------------------------------------\n")
        f.write("\nGoogle\n")
        google(f)

        f.write("-------------------------------------------------\n")
        f.write("\nSkyscanner\n\n")
        skyscanner(f)
        
        f.write("-------------------------------------------------\n")
        f.write("Kayak\n")
        kayak_map(f)


def kayak_map(f):
    """Goes throught the kayak map to find the cheapest flight worldwide"""
    
    # Search by regions
    # Central + South America (Budget set lower)
    f.write("\nCentral America\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-258cy?budget="+"250"
    kayak_finder(link, f)
    
    # Southern Africa
    f.write("\nSouthern Africa\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-2001945fr?budget="+BUDGET
    kayak_finder(link, f)

    # Northen Africa + Southern europe + Middle East
    f.write("\nMediterranean\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-2000178fr?budget="+BUDGET
    kayak_finder(link, f)

    # Cental + Eastern Europe
    f.write("\nEurope\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-2001913fr?budget="+BUDGET
    kayak_finder(link, f)

    # East Asia
    f.write("\nAsia\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-121cy?budget="+BUDGET
    kayak_finder(link, f)

    # Asia
    link = "https://www.kayak.com/explore/"+AIRPORT+"-2001893fr?budget="+BUDGET
    kayak_finder(link, f)

    # Australia
    f.write("\nAustralia\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-177cy?budget="+BUDGET
    kayak_finder(link, f)

    # Pacific Islands 
    f.write("\nPacific Islands\n\n")
    link = "https://www.kayak.com/explore/"+AIRPORT+"-159cy?budget="+BUDGET
    kayak_finder(link, f)

def kayak_finder(link, f):
    """Filters the flights"""

    f.write("link:\n"+link+"\n\n")

    # Retrieve HTML and destinations
    driver.get(link)
    time.sleep(10)
    try:
        WebDriverWait(driver,  5).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@class, "Blek Blek-wrapper Blek-mod-with-title Blek-pres-explore Blek-mod-radius-small Blek-mod-variant-default")]')))    
        soup = BeautifulSoup(driver.page_source, "html.parser")
        destinations = soup.find_all("div", class_="Blek Blek-wrapper Blek-mod-with-title Blek-pres-explore Blek-mod-radius-small Blek-mod-variant-default")
    except TimeoutException:
        destinations = []
        
    # Navigate through given destinations
    for destination in destinations:
        # Write down each city and their prices
        result = destination.text.split(" (")
        city = result[0]
        price = (result[-1].split("$"))[1]

        # Check if city is in the final list or in the scratch list
        if (city not in scratch_locations):
            try:
                f.write(city+"\n"+price+"\n\n")
            except UnicodeEncodeError:
                f.write("Cant encode city name\n"+price+"\n\n")


def google(f):
    """Goes through google flights world map"""

    # Search by regions
    # Central America (lower budget flights)
    f.write("\nCentral America\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxooagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyDAgEEggvbS8wMXR6aBooagwIBBIIL20vMDF0emgSCjIwMjItMTAtMzFyDAgCEggvbS8wMWN4X3ACggENCP___________wEQA0ABSAGYAQGyAQIgAQ&tfu=GgA"
    google_finder(link, f, "250")
    
    # Caribbean (lower budget flights)
    f.write("\nCaribbean\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxooagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyDAgEEggvbS8wMjYxbRooagwIBBIIL20vMDI2MW0SCjIwMjItMTAtMzFyDAgCEggvbS8wMWN4X3ACggENCP___________wEQA0ABSAGYAQGyAQIgAQ&tfu=GgA"
    google_finder(link, f,"250")

    # Africa
    f.write("\nAfrica\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxopagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyDQgEEgkvbS8wZGczbjEaKWoNCAQSCS9tLzBkZzNuMRIKMjAyMi0xMC0zMXIMCAISCC9tLzAxY3hfcAKCAQ0I____________ARADQAFIAZgBAbIBAiAB&tfu=GgA"
    google_finder(link, f, BUDGET)

    # Europe   
    f.write("\nEurope\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxooagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyDAgEEggvbS8wMmo5ehooagwIBBIIL20vMDJqOXoSCjIwMjItMTAtMzFyDAgCEggvbS8wMWN4X3ACggENCP___________wEQA0ABSAGYAQGyAQIgAQ&tfu=GgA"
    google_finder(link, f, BUDGET)

    # Asia
    f.write("\nAsia\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxonagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyCwgEEgcvbS8wajBrGidqCwgEEgcvbS8wajBrEgoyMDIyLTEwLTMxcgwIAhIIL20vMDFjeF9wAoIBDQj___________8BEANAAUgBmAEBsgECIAE&tfu=GgA"    
    google_finder(link, f, BUDGET)

    # Oceania
    f.write("\nOceania\n\n")
    link = "https://www.google.com/travel/explore?tfs=CBwQAxooagwIAhIIL20vMDFjeF8SCjIwMjItMTAtMjdyDAgEEggvbS8wNW5yZxooagwIBBIIL20vMDVucmcSCjIwMjItMTAtMzFyDAgCEggvbS8wMWN4X3ACggENCP___________wEQA0ABSAGYAQGyAQIgAQ&tfu=GgA"    
    google_finder(link, f, BUDGET)

def google_finder(link, f, budget):
    """Filters google map flights"""

    f.write("link:\n"+link+"\n\n")

    # Retrieve HTML and destinations
    driver.get(link)
    time.sleep(3)
    try:
        WebDriverWait(driver,  10).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@class, "dPeLZd")]')))    
        soup = BeautifulSoup(driver.page_source, "html.parser")
        destinations = soup.find_all("div", class_="dPeLZd")
    except TimeoutException:
        destinations = []

    # Navigate through given destinations
    for destination in destinations:
        # Write down each city and their prices
        result = destination.text.split("$")
        city = result[0]
        price = result[1].replace(',', '')

        # Check if city is in the final list or in the scratch list
        if (((int(price)<int(budget))and (city not in scratch_locations))):
            f.write(city+"\n"+price+"\n\n")


def skyscanner(f):
    """Goes to the skyscanner and finds all flights lower than the budget"""
    link = "https://www.skyscanner.com/transport/flights-from/"+AIRPORT
    f.write("link:\n"+link+"\n\n")

    # Retrieve HTML
    driver.get(link)
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@class, "browse-data-route")]')))        
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all the destinations
    destinations = soup.find_all("div", class_="browse-data-route")

    # Iterate until price equals to budget
    i = 1
    price = "0"
    while int(price)<int(BUDGET):
        # find price and city
        result = destinations[i].text
        result = (result.split("from $"))
        city = result[0].replace("\n", "")
        price = result[1].replace("\n", "")
        f.write(city+"\n"+price+"\n\n")
        i+=1

explore()
