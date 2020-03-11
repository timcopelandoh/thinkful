import numpy as np

# --- Question 1 ---
'''
multiples = []

N = 1000

for n in range(1,N):
    if n % 3 == 0 or n % 5 == 0:
        multiples.append(n)

print('Question 1:')    
print(sum(multiples))
print('')


# --- Question 2 ---

fib = [1,2]

new_element = 3

while new_element <=4000000:
    n = len(fib)
    new_element = fib[n-1] + fib[n-2]
    fib.append(new_element)

print('Problem 2:')
print(sum([x for x in fib if x % 2 == 0]))
print('')


# --- Question 3 ---
'''
def primes_below(n):
	nums = [x for x in range(2,n+1)]
	for num in nums:
		for multiple in [m*num for m in range(2,n//num+1)]:
			try:
				nums.remove(multiple)
			except:
				pass
	return nums

primes = primes_below(10000)
new_prod = 1

prime_factors = []

n = 600851475143



def prime_factorization(n, max_prime):
	primes = primes_below(max_prime)
	new_prod = 1
	prime_factors = []
	while new_prod < n:
		if n % (primes[0]*new_prod) == 0:
			new_prod *= primes[0]
			prime_factors.append(primes[0])
		else:
			primes.remove(primes[0])
	return prime_factors
#print('Problem 3:')
#print(prime_factorization(n,10000))
#print('')

'''
# --- Problem 4 ---

def is_palindrome(x):
	x = str(x)
	return x == x[::-1]

for x in range(900,1000):
	for y in range(x,1000):
		if is_palindrome(x*y):
			print(x*y)
'''



# --- Problem 5 ---
'''
n = 2*3*5*7*11*13*17*19

#print(n)

def divisible_by_all(n, max):
	bool_list = [n % x == 0 for x in range(1,max+1)]
	return sum(bool_list) == len(bool_list)


def max_divisible_by_all(max):
	n = np.prod(primes_below(max))
	n_orig = np.prod(primes_below(max))
	success = False
	while success == False:
		if divisible_by_all(n,max):
			print(n)
			success = True
		else:
			n += n_orig

print('Problem 5:')
print(max_divisible_by_all(20))
print('')


# --- Problem 6 ---

n=100

print('Problem 6:')
print(sum(range(n+1))**2 - sum([x**2 for x in range(n+1)]))
print('')


# --- Problem 7 ---


print('Problem 7:')
print(primes_below(150000)[10000])
print('')

# --- Problem 8 ---

str = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

l = 13

max_prod = 0

for i in range(l,len(str)+1):
	max_prod = max([max_prod, np.prod([int(x) for x in str[i-l:i]])])

print(max_prod)



# --- Problem 9 ---

print('Problem 9:')

for a in range(1,1000):
	for b in range(a,1000):
		if a**2 + b**2 == (1000-a-b)**2:
			print('a: {}   b: {}   c: {}'.format(a,b,1000-a-b))
			print('a*b*c = {}'.format(a*b*(1000-a-b)))

print('')
'''


# --- Problem 10 ---

print(sum(primes_below(2000000)))




















