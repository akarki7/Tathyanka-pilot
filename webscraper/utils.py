import pandas as pd


def create_template_A_and_L():
    file = "files/old_data.xlsx"

    cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rows = []
    for x in range(4087, 4149):
        rows.append(x)

    workbook = pd.read_excel(
        file, sheet_name="sample A&L (2)", usecols=cols, skiprows=rows
    )

    for col in workbook.columns:
        if col in ["FYear", "MonthName", "Value"]:
            workbook[col] = ""

    writer = pd.ExcelWriter("templates/TemplateA&L.xlsx", engine="xlsxwriter")
    workbook.to_excel(writer, index=False, sheet_name="Sheet1")
    writer.close()


create_template_A_and_L()
