# Week2, Problem Set 2, #3: Using bisection search to make the program faster
#
# Eliminate slow code

def finalBalance(balance):
	low = balance / 12.0
	high = (balance * (1 + (annualInterestRate/12.0))**12) / 12.0
	lowestPayment = (high+low)/2.0

    for month in range(12):
        minimumMonthlyPayment = balance * (annualInterestRate/12.0)
		monthlyUnpaidBalance = balance - lowestPayment
		balance = monthlyUnpaidBalance + ((annualInterestRate/12.0) * monthlyUnpaidBalance)
	while balance >= 0:
		if lowestPayment * 12.0 < balance:
			lowestPayment = low
		else:
			lowestPayment = high
	return lowestPayment

print finalBalance(3329)



    