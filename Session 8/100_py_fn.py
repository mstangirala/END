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

# 23. python function to find the area of a circle
def square_area(x):
    return x ** 2

# 24. python program for the sum of first n numbers.
def sum_n_num(n):
    return n * (n + 1)/2

# 25. Python Program to Add two Lists
 
NumList1 = []
NumList2 = []
total = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
for i in range(1, Number + 1):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    
for j in range(Number):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)

# 26. Python Program to find Largest and Smallest Number in a List 

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)
print("The Largest Element in this List is : ", largest)
print("The Index position of Largest Element in this List is : ", max_position)

# 27. Python Palindrome Program using Functions
 
reverse = 0
def integer_reverse(number):
    global reverse
    
    if(number > 0):
        Reminder = number % 10
        reverse = (reverse * 10) + Reminder
        integer_reverse(number // 10)
    return reverse


number = int(input("Please Enter any Number: "))

rev = integer_reverse(number)
print("Reverse of a Given number is = %d" %rev)

if(number == rev):
    print("%d is a Palindrome Number" %number)
else:
    print("%d is not a Palindrome Number" %number)

# 28. Python Program to Swap Two Numbers
 
a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

temp = a
a = b
b = temp

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))

# 29. Python Program to Concatenate Strings

str1 = input("Please Enter the First  String : ")
str2 = input("Please Enter the Second String : ")

concat1 = str1 + str2
print("The Final String After Python String Concatenation = ", concat1)

concat2 = str1 + ' ' + str2
print("The Final After String Concatenation with Space = ", concat2)

# 30. Python Program to find Largest of Three Numbers

a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Either any two values or all the three values are equal")

# 31. Python Program to find Diameter, Circumference, and Area Of a Circle
import math

def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * math.pi * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)

# 32. Python Program to Convert String to Uppercase
 
string = input("Please Enter your Own String : ")

string1 = string.upper()
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

# 33. Python Program to Calculate Simple Interest

princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

simple_interest = (princ_amount * rate_of_int * time_period) / 100

print("\nSimple Interest for Principal Amount {0} = {1}".format(princ_amount, simple_interest))

# 34. Python Program to Map two lists into a Dictionary

keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)

# 35. write a Python function To Calculate Volume OF Cylinder 
def volume(r, h): 
    vol = 22/7 * r * r * h 
    return vol

# 36. Recursive Python function to solve the tower of hanoi  
def TowerOfHanoi(n , source, destination, auxiliary): 
    if n==1: 
        print "Move disk 1 from source",source,"to destination",destination 
        return
    TowerOfHanoi(n-1, source, auxiliary, destination) 
    print "Move disk",n,"from source",source,"to destination",destination 
    TowerOfHanoi(n-1, auxiliary, destination, source) 

n = 4
TowerOfHanoi(n,'A','B','C') 

Python 3 program to find time for a 
# given angle. 
  
# 37. python function to find angle between hour hand and minute hand 
def calcAngle(hh, mm): 
  
    # Calculate the angles moved by 
    # hour and minute hands with  
    # reference to 12:00 
    hour_angle = 0.5 * (hh * 60 + mm) 
    minute_angle = 6 * mm 
  
    # Find the difference between 
    # two angles 
    angle = abs(hour_angle - minute_angle) 
  
    # Return the smaller angle of two 
    # possible angles 
    angle = min(360 - angle, angle) 
  
    return angle 
  
# 38. python function to print all time when angle between hour hand and minute 
# hand is theta 
def printTime(theta): 
  
    for hh in range(0, 12): 
        for mm in range(0, 60): 
            if (calcAngle(hh, mm)==theta): 
                print(hh, ":", mm, sep = "") 
                return
              
    print("Input angle not valid.") 
    return

# 39. write a Python program to reverse a linked list 

class Node: 

    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 

    def __init__(self): 
        self.head = None

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 
        
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next


llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 

print("Given Linked List")
llist.printList() 
llist.reverse() 
print("\nReversed Linked List")
llist.printList() 

# 40. write a Python function to Remove all duplicates from a given string
def removeDuplicate(str): 
    s=set(str) 
    s="".join(s) 
    print("Without Order:",s) 
    t="" 
    for i in str: 
        if(i in t): 
            pass
        else: 
            t=t+i 
    print("With Order:",t) 
    
str1="conondrum"
removeDuplicate(str1) 