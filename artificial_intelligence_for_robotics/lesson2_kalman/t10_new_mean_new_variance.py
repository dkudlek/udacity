#! /usr/bin/env python3
# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean = (1.0 / (var1 + var2)) * ((var2 * mean1) + (var1 * mean2))
    new_var = 1.0 / ((1.0 /var1) + (1.0 /var2))
    return [new_mean, new_var]

print("update \ng1(mu=10, sig_sqr=8) and \ng2(mu=13, sig_sqr=2)")
[mu, sig_sqr] = update(10.,8.,13., 2.)
print("mu=", mu," sig_sqr=",sig_sqr)
