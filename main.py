import csv

import numpy as np

def main():
	"""
		Get max trading profits.
	"""
	stop_loss = .15
	data = []
	trades = []
	limit = 60
	file = 'D:/Companies/Biarri/drive-download-20220427T220333Z-001/data_3600.csv'
	with open(file, mode='r', encoding='utf-8-sig') as inFile:
		r = csv.DictReader(inFile)
		for row in r:
			data.append({'time': row['Time'], 'price': row['Price']})

	i = 0
	while i < len(data):
		arr = np.array(data)
		arr = arr[i:i+limit]
		arr = list(arr)
		arr.sort(key=lambda x: (x["price"], x["time"]))
		if int(arr[0]['time']) < int(arr[-1]['time']):
			profit = float(arr[-1]['price']) - float(arr[0]['price'])
			trades.append(profit)
			print(f"Open at {arr[0]['time']} {arr[0]['price']}, close {arr[-1]['time']} {arr[-1]['price']} for {'{:.3f}'.format(profit)}")
			i = limit + int(arr[-1]['time'])
		else:
			i = limit + int(arr[-1]['time'])

	print(f"Total Profit: {'{:.3f}'.format(sum(trades))}")
if __name__=='__main__':
	main()
