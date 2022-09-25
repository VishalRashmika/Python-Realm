
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
   

   # take input from the user
   choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
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
         choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
         print(choice)
         print("Done. Terminating")
         exit()
      else:
         num2 = input("Enter second number: ")
         print(num2)
         addition = float(num1) + float(num2)
         print(num1 +'.0 + ' + num2 + '.0 = ' + str(addition))


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
         choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
         print(choice)
         print("Done. Terminating")
         exit()

      else:
         
         print("float division by zero")

         division = float(num1) + float(num2)
         print(num1 +'.0 / ' + num2 + '.0 = ' + 'None')
   
   elif (choice == '-'):
      num1 = input("Enter first number: ")
      print(num1)
      num2 = input("Enter second number: ")
      print(num2)
      print("Done. Terminating")
      exit()
      
