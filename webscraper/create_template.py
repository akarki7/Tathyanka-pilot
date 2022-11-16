import pandas as pd

file = "BHADRA.xlsx"

cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = []
for x in range(4087, 4149):
    rows.append(x)
workbook = pd.read_excel(file, sheet_name="sample A&L (2)", usecols=cols, skiprows=rows)

for col in workbook.columns:
    if col in ["FYear", "MonthName", "Value"]:
        workbook[col] = ""


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("TemplateA&L.xlsx", engine="xlsxwriter")

workbook.to_excel(writer, index=False, sheet_name="Sheet1")

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Close the Pandas Excel writer and output the Excel file.
writer.close()
