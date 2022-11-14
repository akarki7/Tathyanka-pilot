import pymssql
import pandas as pd

conn = pymssql.connect(
    host=r"10.10.11.4",
    user=r"tathyanka_user",
    password=r"Super@dm1n",
    database="Tathyanka",
)
cursor = conn.cursor(as_dict=True)
cursor.execute("Select * FROM V_DepositLendingTrendByYearMonth")
data = cursor.fetchall()
data_df = pd.DataFrame(data)

print(data_df)

cursor.close()
