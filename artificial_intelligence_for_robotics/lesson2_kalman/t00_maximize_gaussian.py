#! /usr/bin/env python3
#For this problem, you aren't writing any code.
#Instead, please just change the last argument
#in f() to maximize the output.

from math import *

def gauss(mu, sigma_sqr, x):
    return 1/sqrt(2.*pi*sigma_sqr) * exp(-.5*(x-mu)**2 / sigma_sqr)

print("Gauss (mu=10.0,sig_sqr=4.0) for x= 10.0: ")
print(gauss(10.,4.,10.)) #Change the 8. to something else!
