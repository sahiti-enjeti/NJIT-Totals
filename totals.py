total = 0

for month in xrange(1, 12+1):
    totalPaid = round(quantity * salePrice, 2)
    total += totalPaid

print("The total is: " + total)
