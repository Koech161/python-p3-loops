#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    #pass
    i = 10
    while i > 0:
        print(i)
        i -= 1
        print('Happy New Year!')

def square_integers(int_list):
    # code goes here!
    #pass
    return [num ** 2 for num in int_list]

def fizzbuzz():
    # code goes here!
    #pass
    results= [
         'FizzBuzz' if num % 3 == 0 and num % 5 == 0
          else 'Fizz' if num % 3 == 0
          else 'Buzz' if num % 5 == 0
          else num
          for num in range(1, 101)
    ]
    for result in results:
      print(result)
