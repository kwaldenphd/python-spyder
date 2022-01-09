# Your Name
# Your email or NetID

# Python in Spyder

"""Q1: Describe your experience installing Anaconda using the available/provided documentation. What did you expect to happen? What challenges did you face? How did you solve them?"""


"""Q2: How is Spyder different than previous IDEs? What do you see as strengths/advantages? What do you see as possible challenges?"""


"""Q3: What type of error does this program return (syntax, runtime, semantic) and why? How would we go about modifying the program to address this error?"""

print('Enter the first number to add: ')
first = input()
print('Enter the second number to add: ')
second = input()
print('Enter the third number to add: ')
third = input()
print('The sum is ' + first + second + third)

"""Q4: What happens when we run this program? What kinds of log messages do we get, and what information do they give us?"""

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s%%)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s%%)' % (n))
  return total

print(factorial(5))
logging.debug('End of program')

"""Q5: Is this program doing what we expect? Where would you go next with debugging or addressing the error?"""



"""Q6: What are your thoughts on this approach to identifying what's happening in your program? What seems appealing? What seems challenging? When or how could this approach be useful?"""



"""Q7: Compare your experience working in different Python IDEs. What seems appealing about each? What seems challenging? Based on this experience, what is your preference, or are there situations in which you'd prefer one over the other?"""

"""Q8: For each concept, describe in your own words and provide an example using Python syntax. Use comments/narrative text to note each part of your answer."""

# print statement, https://github.com/kwaldenphd/python-intro#your-first-program

# string variable, https://github.com/kwaldenphd/python-intro#variables-and-types

# integer variable, https://github.com/kwaldenphd/python-intro#variables-and-types

# concatenation, https://github.com/kwaldenphd/python-lists-strings#concatenation

# arithmetic operators, https://github.com/kwaldenphd/python-intro#operators

# comparison operators, https://github.com/kwaldenphd/python-intro#operators

# list, https://github.com/kwaldenphd/python-lists-strings

# dictionary, https://github.com/kwaldenphd/python-dictionaries-sets#dictionaries

# if, else, elif statements, https://github.com/kwaldenphd/python-conditional-statements#table-of-contents

# for loop, https://github.com/kwaldenphd/python-conditional-statements#table-of-contents

# while loop, https://github.com/kwaldenphd/python-conditional-statements#table-of-contents

# functions, https://github.com/kwaldenphd/python-functions

# pandas dataframe, https://github.com/kwaldenphd/pandas-intro

