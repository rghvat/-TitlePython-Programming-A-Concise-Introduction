"""
Problem 3_4:
Write a function that is complementary to the one in the previous problem that
will convert a date such as June 17, 2016 into the format 6/17/2016.  I
suggest that you use a dictionary to convert from the name of the month to the
number of the month.  For example months = {"January":1, "February":2, ...}.
Then it is easy to look up the month number as months["February"] and so on.
Note that the grader will assume that month names begin with capital letters.
*** Tip: In print statements, commas create a space.  So you may have difficulty
avoiding a space between the 7, 17, and 2016 below and the following comma.  I 
suggest that you build the output as a single string containing the properly 
formatted date and then print that.  You can convert any number to string by 
using str() and tie the parts together using +. Duplicate the format of the 
example output exactly. Everything you need to do this is covered in the 
lectures. ***

Here is a printout of my run for June 17, 2016.

problem3_4("July",17, 2016)
7/17/2016

"""
#%%
def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    month_mapping = {'January':1,
                     "Febuary":2,
                     "March":3,
                     "April":4,
                     "May" : 5,
                     "June" : 6,
                     "July" : 7,
                     "August" : 8,
                     "September" : 9,
                     "October":10,
          "November":11,
          "December":12
          }
    print('{}/{}/{}'.format(month_mapping[mon], day, year))

#problem3_4("July",17, 2016)