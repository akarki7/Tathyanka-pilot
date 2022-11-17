import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine
from urllib.parse import quote_plus

config = dotenv_values(".env")

host_db = config["HOST_db"]
user_db = config["USER_db"]
passw_db = config["PASSWORD_db"]
name_db = config["DATABASE_db"]


def connect_to_database():
    url = f"mssql+pymssql://{user_db}:%s@{host_db}/{name_db}" % quote_plus(passw_db)
    print(url)
    eng = create_engine(url)
    return eng


def create_template_A_and_L():
    file = "files/old_data.xlsx"

    cols = [1, 2, 3, 4, 5, 6, 7, 8]
    rows = []
    for x in range(4088, 4149):
        rows.append(x)

    workbook = pd.read_excel(
        file, sheet_name="sample A&L (2)", usecols=cols, skiprows=rows
    )

    for col in workbook.columns:
        if col in ["FYear", "MonthName", "Value"]:
            workbook[col] = ""

    output_file = "templates/TemplateA&L.xlsx"
    sheet = "Sheet1"
    writer = pd.ExcelWriter(output_file, engine="xlsxwriter")
    workbook.to_excel(writer, index=False, sheet_name=sheet)
    writer.close()

    return output_file, sheet


def add_year_and_monthname(file, sheet, year, month_name):
    workbook = pd.read_excel(file, sheet_name=sheet)

    for col in workbook.columns:
        if col == "FYear":
            workbook[col] = year
        elif col == "MonthName":
            workbook[col] = month_name

    writer = pd.ExcelWriter(file, engine="xlsxwriter")
    workbook.to_excel(writer, index=False, sheet_name=sheet)
    writer.close()


def add_values(file, sheet, values, new_file, new_sheet):
    workbook = pd.read_excel(file, sheet_name=sheet)

    workbook["Amount"] = values

    writer = pd.ExcelWriter(new_file, engine="xlsxwriter")
    workbook.to_excel(writer, index=False, sheet_name=new_sheet)
    writer.close()


def bulk_insert_sql(file, sheet, table):
    conn = connect_to_database()
    data = pd.read_excel(file, sheet_name=sheet)
    data.to_sql(table, conn, if_exists="append", index=False)
