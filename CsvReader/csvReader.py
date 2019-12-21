import csv

spamReader = csv.reader(open('addition.csv', newline=''), delimiter=' ', quotechar='|')
for row in spamReader:
print(', '.join(row))
