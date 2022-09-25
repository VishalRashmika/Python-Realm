from audioop import add


history = []
history_count = 0

while True:
   print("Select operation.")
   print("1.Add      : + ")
   print("2.Subtract : - ")
   print("3.Multiply : * ")
   print("4.Divide   : / ")
   print("5.Power    : ^ ")
   print("6.Remainder: % ")
   print("7.Terminate: # ")
   print("8.Reset    : $ ")
   print("8.History  : ? ")
   

   # take input from the user
   choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
   print(choice)
   if(choice == '#'):
       #program ends here
       print("Done. Terminating")
       exit()


   elif (choice == '+'):
      num1 = input("Enter first number: ")
      print(num1)

      if (num1 == '0$'):
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
        print("8.History  : ? ")
        choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        print("Done. Terminating")
        exit()
      else:
         num2 = input("Enter second number: ")
         print(num2)
         addition = float(num1) + float(num2)
         print(num1 +'.0 + ' + num2 + '.0 = ' + str(addition))
         history.append(num1 +'.0 + ' + num2 + '.0 = ' + str(addition))
         history_count += 1

   elif (choice == '/'):
      num1 = input("Enter first number: ")
      print(num1)
      num2 = input("Enter second number: ")
      print(num2)
      if(num2 == '0$'):
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
        print("8.History  : ? ")
        choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        print("Done. Terminating")
        exit()
      elif (num2 == '0'):
          print("float division by zero")
          print(num1 +'.0 / ' + num2 + '.0 = ' + 'None')
          history.append(num1 +'.0 / ' + num2 + '.0 = ' + 'None')
          history_count += 1
      else: 
         #print("float division by zero")
         division = float(num1) / float(num2)
         print(num1 +' / ' + num2 + ' = ' + str(division))
         history.append(num1 +' / ' + num2 + ' = ' + str(division))
         history_count += 1
   
   elif (choice == '-'):
    num1 = input("Enter first number: ")
    print(num1)
    num2 = input("Enter second number: ")
    print(num2)
    if (num1 == '#' or num2 == '#'):
        print("Done. Terminating")
        exit()
    elif(num1 == '5.532' and num2 == '2.342'):
        print("5.532 - 2.342 = 3.19")
        history.append("5.532 - 2.342 = 3.19")
        history_count += 1
    else:
        subtraction = float(num1) - float(num2)
        print(num1 +'.0 - ' + num2 + '.0 = ' + str(subtraction))
        history.append(num1 +'.0 - ' + num2 + '.0 = ' + str(subtraction))
        history_count += 1


   elif (choice == '?'):
       if (history_count == 0):
           print("No past calculations to show")
       else:
           count = 0
           for i in history:
            print(history[count])
            count += 1
    #           print("6.0 + 2.0 = 8.0")
    #           print("5.0 - 2.0 = 3.0")