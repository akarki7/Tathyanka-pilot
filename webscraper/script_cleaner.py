import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import openpyxl as xlsx
from utils_scraper import *
import numpy as np

# can comment this DATE out if we want to pass it from the argments directly
# DATE = "207905 BHADRA"
DATE = None

args_parser = argparse.ArgumentParser()

# -o OUTPUT_FILE_NAME
args_parser.add_argument("-of", "--output_file", help="Output file name")
args_parser.add_argument("-d", "--date", help="year and month")
args = args_parser.parse_args()

URL = "https://www.nrb.org.np/category/monthly-statistics/"


def main():
    if not DATE:
        month_name = args.date
    else:
        month_name = DATE

    year = month_name[0:4]

    page = requests.get(URL)

    file_to_extract_data_from = parser(page)
    create_excel(file_to_extract_data_from, month_name, year)


def parser(page):
    soup = BeautifulSoup(page.content, "html.parser")
    # results contains all the <li> that have the data we need
    results = soup.find("ul", class_="arrowed-list arrowed-list--border").find_all("li")

    # NOTE: for our implementation right now I will only use the first <li> to get the latest data only

    file_name = results[0].div.find_all("a")[0].text
    file_url = results[0].div.find_all("a")[2]["href"]
    resp = requests.get(file_url)
    file_name = file_name + ".xls"
    output = open(file_name, "wb")
    output.write(resp.content)
    output.close()

    return file_name


def create_excel(file, month_name, year):
    template_file, sheet = create_template_A_and_L()
    add_year_and_monthname(template_file, sheet, year, month_name)
    values = extract_data_sheet_8(file)
    add_values(template_file, sheet, values, month_name + "_cleaned.xlsx", "A&L")


def extract_data_sheet_8(file):
    """
    workbook.iloc[0] -> gives value of first row
    Unnamed:3 to Unnamed:62 col with values

    Row 1 -> BFI Name
    Row 3 -> CAPITAL FUND
    Row 4 -> a. Paid-Up Capital
    Make hardcode table with fixed value
    Extract data from C8 and store it alongisde the above hardcode value

    0  to 66
    """
    cols = list(range(3, 63))
    rows = [
        0,
        1,
        2,
        3,
        12,
        18,
        19,
        22,
        25,
        28,
        31,
        35,
        42,
        43,
        44,
        45,
        48,
        49,
        52,
        57,
        60,
        66,
        70,
        71,
        75,
        79,
        83,
        84,
        96,
    ]
    workbook = pd.read_excel(file, sheet_name="C8", usecols=cols, skiprows=rows)

    output_list = []
    for x in range(0, 67):
        data = workbook.iloc[x]
        sum = 0
        for d in data:
            if isinstance(d, str):
                d = 0.0
            output_list.append(d)
            sum = sum + d
        output_list.append(round(sum, 6))

    return output_list


main()
