# 1. python function to return the nth fibonacci number
def fib(n):
   if n <= 1:
      return n
   else:
      return (fib(n-1) + fib(n-2))

# 2. python function to return the factorial of a number
def fact(n):
   if n == 1:
      return n
   else:
      return n * fact(n-1)

# 3. python function to return the squares of a list of numbers
def sq(n):
   return [i**2 for i in range(n)]

# 3. python function to return the squareroot of a list of numbers
def sqrt(n):
   return [i**0.5 for i in range(n)]

# 4. python function to add even number from 1st list and odd number from 2nd list
def even_odd(l1, l2):
    return[x + y for x, y in zip(l1, l2) if x % 2 ==0 and y % 2 != 0]

# 5. python function to strip vowels from a string
def strip_vowel_str(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return "".join([x for x in str if x not in vowels])

# 6. python ReLu function
def relu_like_activation(l):
    return[0 if x < 0 else x for x in l]

# 7. python sigmoid function
def sigmoid_activation(l):
    return[round(1/(1+math.exp(-x)),2) for x in l]

#8. python function to identify profane words
def profane_filter(str):
    profane_word_url = "https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt"
    file = urllib.request.urlopen(profane_word_url)
    for line in file:
        decoded_line = line.decode("utf-8")
    return decoded_line
    str = re.findall(r'\w+', str)
    return [i for i in str if i in decoded_line]

# 9. python function to add even mubers in a list
def add_even_num(l):
    sum = reduce(lambda a, b: a + b, filter(lambda a: (a % 2 == 0), l))
    return sum

# 10. python function to find the area of a circle
def circle_area(r):
    return 22/7 * r**2

# 11. python program to find whether a number is prime
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             

# 12. python function to return the cubes of a list of numbers
def cube(n):
   return [i*i*i for i in range(n)]

# 13. python function to find the average of given numbers
def average():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add
a = average()
a(10)
a(20)
a(45)

# 14. python function to create adders
def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x + y)
    return adders
adders = create_adders()

# 15. python function for datetime
from datetime import datetime
datetime.utcnow()
def log(msg, *, dt = datetime.utcnow()):
    print(f'Message at {dt} was {msg}')

# 16. python function for count of address reference
import ctypes
def ref_count(address : int): #what is int doing here? Annotations
    return ctypes.c_long.from_address(address).value

# 17. python function to modify a tuple
def modify_tuple(t):
    print(f'Initial t mem-add = {id(t)}')
    t[0].append(100)
    print(f'Final t mem-add = {id(t)}')

# 18. python program to compare strings
def compare_using_equals(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass

# 19. python program to compare strings using interning
import sys
def compare_using_interning(n):
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    for i in range(n):
        if a is b:
            pass

# 20. python program to calculate the time taken to create a float and decimal
import time
def run_float(n = 1):
    for i in range(n):
        a = 3.1415

def run_decimal(n = 1):
    for i in range(n):
        a = Decimal('3.1415')
n = 10000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()

print ('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()

print ('decimal: ', end - start)

# 21. python function for factorial using reduce
def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n+1))
fact(10)

# 22. python program to find if given co-ordinates are inside circle
from random import uniform
from math import sqrt
def random_shot(rad):
    r_x = uniform(-rad, rad)
    r_y = uniform(-rad, rad)

    if sqrt(r_x**2 + r_y**2) <= rad:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return r_x, r_y, is_in_circle

