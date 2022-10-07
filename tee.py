try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except:
    print("Bug in user input.")











# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b = ", a/b)
#     print("a+b = ", a+b)
# except ValueError:
#     print("Could not convert to a number.")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except:
#     print("Something went very wrong.")








# try:
#  n = int(input("How old are you? "))
#  percent = round(n*100/80, 1)
#  print("You've gone through", percent, "% of your life!")
# except ValueError:
#  print("Oops, must enter a number.")
# except ZeroDivisionError:
#  print("Division by zero.")
# except:
#  print("Something went very wrong.")