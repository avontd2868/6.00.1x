# Week2, Problem Set 2, #1: Paying the Minimum
#
# Calculate the credit card balance after one year if a person only pays the
# minimum monthly payment required by the cc company each month.

total = 0

for month in range(1,13):
	print "Month: %d" % month
	
	monthlyInterestRate = annualInterestRate/12.0
	minimumMonthlyPayment = balance * monthlyPaymentRate
	monthlyUnpaidBalance = balance - minimumMonthlyPayment
	balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
	balance = round(balance,2)

	print "Minimum monthly payment: " + str(round(minimumMonthlyPayment,2))
	print "Remaining balance: "  + str(round(balance,2))

	total += minimumMonthlyPayment

print "Total paid: " + str(round(total,2))
print "Remaining balance: " + str(round(balance,2))
