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

URL = "https://www.nrb.org.np/category/monthly-statistics/"


def main():
    page = requests.get(URL)
    filename = "website.html"

    with open(filename, "w") as f:
        f.write(page.text)

    parser(page)


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


main()
