import pandas as pd
import shutil


def create_template_A_and_L():
    file = "files/old_data.xlsx"

    cols = [1, 2, 3, 4, 5, 6, 7, 8]
    rows = []
    for x in range(4087, 4149):
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

    workbook["Value"] = values

    writer = pd.ExcelWriter(new_file, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name=new_sheet)
    writer.close()
