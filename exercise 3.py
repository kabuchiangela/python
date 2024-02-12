#number =int(input("number: "))
#if number >0:
 #   print("number is positive")
#elif number <0:
 #   print("number is negative")
#elif number == 0:
 #   print("number is 0")
#else:
  #  print("invalid input")

eng = 78
math =73
if eng > 0 and math > 0:
    print("both values are positive")
elif math < 0 and eng < 0:
    print("both are negative")
elif math > 0 or eng > 0:
    print("one of the values is positive")
else:
    print("one or all of the values is zero")