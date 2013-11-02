# Week2, Problem Set 2, #1: Paying the Minimum
#
# Calculate the credit card balance after one year if a person only pays the
# minimum monthly payment required by the cc company each month.

monthlyInterestRate = annualInterestRate / 12.0
lowestPayment = 10


def finalBalance(balance,lowestPayment):
	for month in range(12):
		minimumMonthlyPayment = balance * monthlyInterestRate
		monthlyUnpaidBalance = balance - lowestPayment
		balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
		print balance
	return balance


while finalBalance(balance,lowestPayment) >= 0:
	lowestPayment += 10
    
print "Lowest Payment: " + str(lowestPayment)


    

	


	




