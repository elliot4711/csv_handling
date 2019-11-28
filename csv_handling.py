import csv
from datetime import datetime

path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/csv_handling/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)

data = []
for row in reader:
    date = datetime.strptime(row[0], "%m/%d/%Y")
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = float(row[5])
    adj_close = float(row[5])

data.append([date, open_price, high, low, close, volume, adj_close])
print(data[0])