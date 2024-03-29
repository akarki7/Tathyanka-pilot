import pandas as pd

# Create a Pandas dataframe from some data.
col_FYear = "2079"
col_MonthName = "207905 BHADRA"
col_Category = ["LIABILITIES", "ASSETS"]
col_SubCategory = [
    "1. CAPITAL FUND",
    "2. BORROWINGS",
    "3. DEPOSITS",
    "4. Bills Payable",
    "5. Other Liabilities",
    "6. Reconcillation A/c",
    "7. Profit & Loss A/c",
    "1. LIQUID FUNDS",
    "2. INVESTMENT IN SECURITIES",
    "3. SHARE & OTHER INVESTMENT",
    "4. LOANS & ADVANCES (Including Bills Purchased)",
    "5. LOANS AGAINST COLLECTED BILLS",
    "6. FIXED ASSETS",
    "7. OTHER ASSETS",
    "8. Expenses not Written off",
    "9. Non Banking Assets",
    "10. Reconcillation Account",
    "11. Profit & Loss A/c",
]
col_AccountHead = [
    "a. Paidup Capital",
    "b. Calls in Advance",
    "c. Proposed Bonus Share",
    "d. General Reserves",
    "e. Share Premium",
    "f. Retained Earning",
    "g. Others Reserves Fund",
    "a. NRB",
    "b. Interbank Borrowing",
    "c. Foreign Banks and Fin. Ins.",
    "d. Other Financial Ins.",
    "e. Bonds and Securities",
    "a. Current",
    "b. Savings",
    "c. Fixed",
    "d. Call Deposits",
    "e. Others",
    "a. Bills Payable",
    "a. Sundry Creditors",
    "b. Loan Loss Provision",
    "c. Interest Suspense a/c",
    "d. Others",
    "a. Reconcillation A/c",
    "a. Profit & Loss A/c",
    "a. Cash Balance",
    "b. Bank Balance",
    "c. Money at Call",
    "a. Govt.Securities",
    "b. NRB Bond",
    "c. Govt.NonFin. Ins.",
    "d. Other NonFin. Ins.",
    "e  Non Residents",
    "a. Interbank Lending",
    "b. Non Residents",
    "c.  Others",
    "a. LOANS & ADVANCES",
    "b. BILL PURCHASED",
    "a. Against  Domestic Bills",
    "b. Against Foreign Bills",
    "a. FIXED ASSETS",
    "a. Accrued Interest",
    "b.  Staff Loans / Adv.",
    "c.  Sundry Debtors",
    "d.  Cash In Transit",
    "e.  Others",
    "a. Expenses not Written off",
    "a. Non Banking Assets",
    "a. Reconcillation Account",
    "a. Profit & Loss A/c",
]
col_SubHead1 = [
    "a. Paidup Capital",
    "b. Calls in Advance",
    "c. Proposed Bonus Share",
    "d. General Reserves",
    "e. Share Premium",
    "f. Retained Earning",
    "g. Others Reserves Fund",
    "a. NRB",
    "b. Interbank Borrowing",
    "c. Foreign Banks and Fin. Ins.",
    "d. Other Financial Ins.",
    "e. Bonds and Securities",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "a. Bills Payable",
    "a. Sundry Creditors",
    "b. Loan Loss Provision",
    "c. Interest Suspense a/c",
    "d. Others",
    "a. Reconcillation A/c",
    "a. Profit & Loss A/c",
    "1. Nepalese Notes & Coins",
    "2. Foreign Currency",
    "1. In Nepal Rastra Bank",
    '2. "A"Class Licensed Institution',
    "3. Other Financial Ins.",
    "4. In Foreign Banks",
    "1. Domestic Currency",
    "2. Foreign Currency",
    "a. Govt.Securities",
    "b. NRB Bond",
    "c. Govt.NonFin. Ins.",
    "d. Other NonFin. Ins.",
    "e  Non Residents",
    "a. Interbank Lending",
    "b. Non Residents",
    "c. Others",
    "1. Private  Sector",
    "2. Financial Institutions",
    "3. Government Organizations",
    "1. Domestic Bills Purchased",
    "2. Foreign Bills Purchased",
    "3. Import Bills & Imports",
    "a. Against  Domestic Bills",
    "b. Against Foreign Bills",
    "a. FIXED ASSETS",
    "1. Financial Institutions",
    "2. Government  Enterprises",
    "3. Private Sector",
    "b.  Staff Loans / Adv.",
    "c.  Sundry Debtors",
    "d.  Cash In Transit",
    "e.  Others",
    "a. Expenses not Written off",
    "a. Non Banking Assets",
    "a. Reconcillation Account",
    "a. Profit & Loss A/c",
]
col_SubHead2 = [
    "a. Paidup Capital",
    "b. Calls in Advance",
    "c. Proposed Bonus Share",
    "d. General Reserves",
    "e. Share Premium",
    "f. Retained Earning",
    "g. Others Reserves Fund",
    "a. NRB",
    "b. Interbank Borrowing",
    "c. Foreign Banks and Fin. Ins.",
    "d. Other Financial Ins.",
    "e. Bonds and Securities",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "1. Domestic",
    "2. Foreign",
    "a. Bills Payable",
    "a. Sundry Creditors",
    "b. Loan Loss Provision",
    "c. Interest Suspense a/c",
    "d. Others",
    "a. Reconcillation A/c",
    "a. Profit & Loss A/c",
    "1. Nepalese Notes & Coins",
    "2. Foreign Currency",
    "i. Domestic Currency",
    "ii. Foreign Currency",
    "i. Domestic Currency",
    "ii. Foreign Currency",
    "3. Other Financial Ins.",
    "4. In Foreign Banks",
    "1. Domestic Currency",
    "2. Foreign Currency",
    "a. Govt.Securities",
    "b. NRB Bond",
    "c. Govt.NonFin. Ins.",
    "d. Other NonFin. Ins.",
    "e  Non Residents",
    "a. Interbank Lending",
    "b. Non Residents",
    "c. Others",
    "1. Private  Sector",
    "2. Financial Institutions",
    "3. Government Organizations",
    "1. Domestic Bills Purchased",
    "2. Foreign Bills Purchased",
    "3. Import Bills & Imports",
    "a. Against  Domestic Bills",
    "b. Against Foreign Bills",
    "a. FIXED ASSETS",
    "1. Financial Institutions",
    "2. Government  Enterprises",
    "3. Private Sector",
    "b.  Staff Loans / Adv.",
    "c.  Sundry Debtors",
    "d.  Cash In Transit",
    "e.  Others",
    "a. Expenses not Written off",
    "a. Non Banking Assets",
    "a. Reconcillation Account",
    "a. Profit & Loss A/c",
]
col_Attribute = [
    "NBL",
    "RBB",
    "NABIL",
    "NIBL",
    "SCBNL",
    "HBL",
    "NSBI",
    "EBL",
    "BOK",
    "NCC",
    "NIC",
    "MBL",
    "Kumari",
    "Laxmi",
    "SBL",
    "ADBNL",
    "Global",
    "Citizen",
    "Prime",
    "Sunrise",
    "NMB",
    "Prabhu",
    "Mega",
    "CBL",
    "Century",
    "Sanima",
    "Mahalaxmi",
    "Narayani",
    "Karnali",
    "Shangrila",
    "Excel",
    "Miteri",
    "Mukti",
    "Garima",
    "Kamana",
    "Corporate",
    "Jyoti",
    "Shine",
    "LumbiniDB",
    "Sindhu",
    "Salapa",
    "Saptakoshi",
    "GreenDB",
    "NFL",
    "NSML",
    "GURKHAFC",
    "Goodwill",
    "Shree",
    "BestFC",
    "Progressive",
    "Janaki",
    "Pokhara",
    "Central",
    "Multi",
    "Samriddhi",
    "CMerchant",
    "GMBFL",
    "ICFC",
    "Manju",
    "Reliance",
    "OVERALL",
]
col_Value = []

print(len(col_Attribute))

# df = pd.DataFrame(
#     {
#         "FYear": col_FYear,
#         "MonthName": col_MonthName,
#         "Category": col_Category,
#         "SubCategory": col_SubCategory,
#         "AccountHead": col_AccountHead,
#         "SubHead1": col_SubHead1,
#         "SubHead2": col_SubHead2,
#         "Attribute": col_Attribute,
#         "Value": col_Value,
#     }
# )
# df = df.reset_index(drop=True)

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter("pandas_header_format.xlsx", engine="xlsxwriter")

# # Convert the dataframe to an XlsxWriter Excel object. Note that we turn off
# # the default header and skip one row to allow us to insert a user defined
# # header.
# df.to_excel(writer, index=False, sheet_name="Sheet1", startrow=1, header=False)

# # Get the xlsxwriter workbook and worksheet objects.
# workbook = writer.book
# worksheet = writer.sheets["Sheet1"]


# # Write the column headers with the defined format.
# for col_num, value in enumerate(df.columns.values):
#     worksheet.write(0, col_num, value)

# # Close the Pandas Excel writer and output the Excel file.
# writer.close()
