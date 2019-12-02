import csv

with open('csv_data.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow([["data", "test"]])
writeFile.close()

with open('csv_data.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	data = list(reader)
	
print(data)