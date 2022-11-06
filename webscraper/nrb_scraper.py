"""
Imp notes:

Webite to scrape data from: https://www.nrb.org.np/category/monthly-statistics/?department=bfr
https://www.nrb.org.np/category/monthly-statistics/ -> This same as above but does not have the left
bar that had some oter optons but the files that we need are the same

?key=vaue -> query

?key1=value1&key2=value2 -> & is the separator here that separates multiple queries

URL encoding normally replaces a space with a plus (+) sign or with %20




"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.nrb.org.np/category/monthly-statistics/"


def main():
    page = requests.get(URL)

    # filename = "website.html"
    # with open(filename, "w") as f:
    #     f.write(page.text)

    file_to_extract_data_from = parser(page)

    extract_and_store(file_to_extract_data_from)


def parser(page):
    soup = BeautifulSoup(page.content, "html.parser")
    # results contains all the <li> that have the data we need
    results = soup.find("ul", class_="arrowed-list arrowed-list--border").find_all("li")

    # NOTE: for our implementation right now I will only use the first <li> to get the latest data only

    file_name = results[0].div.find_all("a")[0].text
    file_url = results[0].div.find_all("a")[2]["href"]
    resp = requests.get(file_url)
    output = open(file_name + ".xls", "wb")
    output.write(resp.content)
    output.close()

    return file_name


def extract_and_store(file):
    workbook = pd.read_excel(file + ".xls", sheet_name="C4")
    indicators_types_list = get_indicators_types(workbook)
    major_financial_indicators = {}

    bank_types = ["Class 'A'", "Class 'B'", "Class 'C'", "Overall"]
    bank_index_in_sheet = ["Unnamed: 3", "Unnamed: 4", "Unnamed: 5"]
    range_list = [(4, 14), (16, 18), (20, 21), (23, 34), (36, 40)]

    credit_deposit_ratios = get_data_from_column(workbook, "Unnamed: 2", range_list[0])
    liquidity_ratios = get_data_from_column(workbook, "Unnamed: 2", range_list[1])
    capital_adequacy_ratios = get_data_from_column(
        workbook, "Unnamed: 2", range_list[2]
    )
    financial_access = get_data_from_column(workbook, "Unnamed: 2", range_list[3])

    for x, y in zip(bank_types, bank_index_in_sheet):
        major_financial_indicators[x] = get_data_class_wise(
            indicators_types_list,
            range_list,
            y,
            credit_deposit_ratios,
            liquidity_ratios,
            capital_adequacy_ratios,
            financial_access,
        )

    # pd.set_option("display.max_rows", None, "display.max_columns", None)
    # major_financial_indicators_dataframe = pd.DataFrame.from_dict(
    #     pad_dict_list(major_financial_indicators, None)
    # )
    # print(workbook)


def get_indicators_types(workbook) -> list:
    indicators_types_list = []
    index_list = [3, 15, 19, 22, 35]
    for x in index_list:
        indicators_types_list.append(workbook["Unnamed: 1"].iloc[x])

    return indicators_types_list


def get_data_from_column(workbook, column_name, row_range) -> list:  # row_range = tuple
    data_list = []
    for x in range(row_range[0], row_range[1] + 1):
        data_list.append(workbook[column_name].iloc[x])

    return data_list


def get_data_class_wise(
    indicators_types_list,
    range_list,
    class_index,
    credit_deposit_ratios,
    liquidity_ratios,
    capital_adequacy_ratios,
    financial_access,
):
    """Return =
    {
    "A.  Credit, Deposit Ratios (%)": {
        "Fixed Deposit/Total Deposit": 92,
        "Total Deposit/GDP": 56,
    },
    "B.  Liquidity Ratios (%)": {
        "Cash & Bank Balance/Total Deposit": 7.10,
        "Total LA": 24.97,
    },
    "C.  Capital Adequacy Ratios (%)": {
        "Core Capital": 7.10,
        "Total Capital": 24.97,
    },
    "D.  Financial Access": {
        "No. of institutions": 7.10,
        "No. of Deposit Accounts": 24.97,
    }
    """

    # get index value in for loop
    """
    if index=0, then use credit_deposit_ratios,
    if index =1, then use liquidity_ratios and so on

    or change the sent data like this:

    {0: credit_deposit_ratios, }
    then do dict.get(str(index_of_loop))
    """

    data = {}
    for x, y in zip(indicators_types_list, range_list):
        data[x] = {}


def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list


main()
