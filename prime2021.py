# 2021 PRIMES

import numpy as np
import matplotlib.pyplot as plt 

# Max value
N = 17580

# Create an array of odd numbers up to N
# Then replace 1 with 2 (the first prime number)
primes = np.arange(1,N,2)
primes[0]=2

# Use Sieve of Eratosthenes to eliminate all non prime numbers
for i in range(int(np.sqrt(N))+1):
    # Get the value in the primes array
    p = primes[i]
    
    # Remove all number in the prime array that are divisible by but 
    # not equal to the selected value
    primes = primes[[(d == p or d % p != 0) for d in primes]]

    # Repeat until all non-primes are removed

# Create an array of all numbers up to the max prime found
all_num = np.arange(1,np.max(primes),1)

# Plot on a polar plot where 
# radius = pr
# angle = pr

fig = plt.figure(figsize=[15,15])
ax = fig.add_subplot(111,polar=True)
ax.grid(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.style.use('dark_background')
ax.spines['polar'].set_visible(False)

ax.plot(all_num, all_num, 
        linestyle="none", marker=".", markersize=1, 
        color="white")

ax.plot(primes, primes, 
        linestyle="none", marker=".", markersize=10, 
        color="red")

plt.title("2021 Primes", fontsize="30")
ax.text(0.5, -0.01, "r = primes, θ = primes", transform=ax.transAxes, 
        fontsize=25, color="red",
        verticalalignment='top', horizontalalignment="center")

ax.text(0.5, -0.05, "r = integers, θ = integers", transform=ax.transAxes, 
        fontsize=25, color="white",
        verticalalignment='top', horizontalalignment="center")
