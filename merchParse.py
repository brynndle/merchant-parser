# Simple CSV Merchant Parser
# Written by David Caputo

import os
import csv

# Merchant to search on
print "\n"
merchant = raw_input("Enter merchant name: ")

num_emails = 0

# Row 3 = Merchant name
# Row 4 = Customer First Name
# Row 5 = Customer Last Name
# Row 6 = Customer Email
# Row 8 = Last Visit
# Row 9 = Visit Count

filename = merchant + ".csv"


f = open('CustomerRelationship-20150819.csv')

emails_f = csv.writer(open(filename, "wb+"))
emails_f.writerow(["First Name", "Email", "Last Visit", "Visit Count"])

csv_f = csv.reader(f)

for row in csv_f:
	if row[3] == merchant and row[6] != "":
		emails_f.writerow([row[4], row[6], row[8], row[9]])
		num_emails += 1
if num_emails > 0:
	print "File created with", num_emails, "customer emails. \n"
else:
	os.remove(filename)
	print "Mercant not found."

f.close()