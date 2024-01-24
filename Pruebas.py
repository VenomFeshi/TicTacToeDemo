# def is_year_leap(year):
#     #
    # if year %4 == 0 and year %100 == 0 and year %400 == 0:
    #     return True
    # elif year %4 == 0 and year %100 != 0:
    #     return True
    # else:
    #     return False
#     #

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

########################################################################################

# def is_year_leap(year):
#     if year %4 == 0 and year %100 == 0 and year %400 == 0:
#         return True
#     elif year %4 == 0 and year %100 != 0:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     months_allowed = list(range(1,13))
#     if month in months_allowed:
#         # days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if month %2 != 0 and month <= 7: #even return 31 days
#             return 31
#         elif month %2==0 and month == 2: #for February
#             if is_year_leap(year):
#                 return 29 #leap year
#             else:
#                 return 28 #not leap year
#         elif month %2 == 0 and month <= 7:
#             return 30
#         elif month %2 == 0 and month > 7:
#             return 31
#         else:
#             return 30
    
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 7, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

########################################################################################

# def is_year_leap(year):
#     if year %4 == 0 and year %100 == 0 and year %400 == 0:
#         return True
#     elif year %4 == 0 and year %100 != 0:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     months_allowed = list(range(1,13))
#     if month in months_allowed:
#         if month %2 != 0 and month <= 7: #even return 31 days
#             return 31
#         elif month %2==0 and month == 2: #for February
#             if is_year_leap(year):
#                 return 29 #leap year
#             else:
#                 return 28 #not leap year
#         elif month %2 == 0 and month <= 7:
#             return 30
#         elif month %2 == 0 and month > 7:
#             return 31
#         else:
#             return 30

# def day_of_year(year, month, day):
#     if is_year_leap(year):
#         for i in range(1,month):
#             day = day + days_in_month(year, i)
#         return day
#     else:
#         for i in range(1,month):
#             day = day + days_in_month(year, i)
#         return day

# print(day_of_year(2001, 12, 31))

########################################################################################
# def is_year_leap(year):
#     if year %4 == 0 and year %100 == 0 and year %400 == 0:
#         return True
#     elif year %4 == 0 and year %100 != 0:
#         return True
#     else:
#         return False
    
# def day_of_year(year, month, day):
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_year_leap(year):
#         day += 1
#         for i in range(0,month-1):
#             day += days_in_month[i]
#         return day
#     else:
#         for i in range(0,month-1):
#             day += days_in_month[i]
#         return day

# print(day_of_year(2000, 6, 31))

########################################################################################

# def is_prime(num,divisibles):
#     if num <=9:
#         for j in range(2, num):
#             if num %j == 0:
#                 return False
#         return True
#     else:   
#         for j in range(2, len(divisibles)):
#             if num %j == 0:
#                 return False
#         return True
    
# divisibles = list(range(1,9))
# # print(len(divisibles))
# for i in range(1, 100):
#     if is_prime(i + 1,divisibles):
#         print(i + 1, end=" ")
# print()

########################################################################################

# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

# def liters_100km_to_miles_gallon(liters): #li/100km to mi/gal
#     gallons = liters/3.785411784
#     mile = 1/(1609.344/1000/100)
#     transformation = mile/gallons
#     return transformation

# def miles_gallon_to_liters_100km(miles): #mi/gal to li/100km
#     liters = 1*3.785411784
#     km100 = miles*(1609.344/1000/100)
#     transformation = liters/km100
#     return transformation

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))



########################################################################################

# km_to_miles = 0.621371
# gram_to_pounds = 0.00220462
# hour_to_seconds = 3600
# celsius_to_fahrenheit = (c * 9/5) + 32
# ml_to_fl_ounces = 0.033814

########################################################################################

# def is_a_triangle(a,b,c):
#     return (a+b > c) and (a+c > b) and (b+c > a)

# values = []
# while len(values) < 3:
#     values.append(float(input("Enter a value number: ")))

########################################################################################

# def factorial(num):
#     aux = num
#     if num >0:
#         for i in range(num-1,1,-1):
#             aux *= i
#         return aux
#     if num == 0:
#         return 1
#     else:
#         return False

# value = int(input("Enter the factorial value you want to calculate: "))
# print(factorial(value))

########################################################################################

# def fib(num):
#     first = second = 1
#     if num > 2:
#         for i in range(0,num-2):
#             value = first + second
#             second, first = first, value
#         return value
#     if num == 1 or num == 2:
#         return 1
#     return False

# def fibonacci(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)


# for sequence in range(1, 11):
#     print(sequence, fibonacci(sequence))

# sequence = 4
# print(fibonacci(sequence))

########################################################################################

# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
 
# print(fun(25))

########################################################################################

# my_tuple = (1, 10, 50, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-3])

# for elem in my_tuple:
#     print(elem)

########################################################################################

# dictionary = {'element':(0.,)}

# my_tuple = (1.,)
# your_tuple = (2.,)

# dictionary['element'] += my_tuple
# dictionary['element'] += your_tuple

# print(dictionary)
# print(my_tuple+your_tuple)

########################################################################################

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# # print(dictionary)
# # print(phone_numbers)
# # print(empty_dictionary)

# print(dictionary['cat'])
# print(phone_numbers['boss'])
# # print(phone_numbers['president']) #can cause an Error 
# print(len(dictionary))
# print(phone_numbers.keys())

# for english, french in dictionary.items():
#     print(english, "->" ,french)

########################################################################################

# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break

#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
    
#     if name in school_class:
#         school_class[name] += (score,)
        
#     else:
#         school_class[name] = (score,)

# print(school_class)

# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

########################################################################################

# tup = 1,2,3
# a,b,c = tup 
# print(a,b,c,a*b*c)

########################################################################################

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # outputs: 4

########################################################################################

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     # Write your code here.

# print(d3)

########################################################################################

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(d1)
#     d3.update(d2)

# print(d3)

########################################################################################

#convert colors tuple into a dictionary

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)

# print(colors_dictionary)

########################################################################################

# inside_code = False

# while not(inside_code):

#     try:
#         number = int(input("Write down a number here: "))
#         print(number)
#         if (not(inside_code)):
#             inside_code = True
#     except:
#         print("remember to write down a number.")

########################################################################################

# try:
#     value = int(input('Enter a natural number: '))
#     result = 1 / value
#     print('The reciprocal of', value, 'is', result)
# except ValueError:
#     print('Invalid input. Please enter a natural number.')
# except ZeroDivisionError:
#     print('Cannot divide by zero.')
# except KeyboardInterrupt:
#     print('\nProgram interrupted by the user.')
# except Exception as e:
#     print(f'An unexpected error occurred: {e}')
# else:
#     print('No exceptions occurred. Program execution completed successfully.')
# finally:
#     print('This block always executes, whether an exception occurred or not.')

########################################################################################

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")