# Simple CSV Merchant Parser
# Written by David Caputo

import csv

# Merchant to search on
merchant = "EVL PDX"


# Row 3 = Merchant name
# Row 4 = Customer First Name
# Row 5 = Customer Last Name
# Row 6 = Customer Email
# Row 8 = Last Visit
# Row 9 = Visit Count

f = open('CustomerRelationship-20150819.csv')

emails_f = csv.writer(open("emails.csv", "wb"))
emails_f.writerow(["First Name", "Email", "Last Visit", "Visit Count"])

csv_f = csv.reader(f)

for row in csv_f:
	if row[3] == merchant and row[6] != "":
		emails_f.writerow([row[4], row[6], row[8], row[9]])

f.close()