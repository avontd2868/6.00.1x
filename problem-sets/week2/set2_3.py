# Week2, Problem Set 2, #3: find minimum payment using bisection search
#
# Eliminate slow

monthlyInterestRate = annualInterestRate/12.0
low = balance / 12.0
high = (balance * (1 + monthlyInterestRate)**12) / 12.0
mid = (high+low) / 2.0


def remainingBalance(monthlyPayment):
	remainingBalance = balance
	for month in range(12):
		unpaidBalance = remainingBalance - monthlyPayment
		remainingBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
	return remainingBalance

for i in range(20):
	if remainingBalance(mid) > 0.00:
		low = mid
	else:
		high = mid
	mid = (high + low) / 2.0

print "Lowest Payment: " + str(round(mid,2))
	

    


	
	




