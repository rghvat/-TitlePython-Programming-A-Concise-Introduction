def problem1_7():
   base1 = input('Enter the length of one of the bases: ')
   base2 = input('Enter the length of the other base: ')
   height = input('Enter the height: ')
   
   print('The area of a trapezoid with bases {} and {} and height {} is {}'.format(float(base1), float(base2), float(height),0.5*(float(base1)+float(base2))*float(height)))
