value = (5, 4, 2000, 2.51, 8, 9, 151)



def menu():
  global value
  option = ''
  while(option != 6):
    print('*** Tuple example ***')
    print('1. Print Tuple ***')
    print('2. Loop over tuple')
    print('3. Copy Tuple')
    print('4. Convert to list')
    print('5. Sort Tuple')
    print('6. Exit ***')
    option = int(input('Please enter option: '))

    if(option == 1):
      print(value)
    elif(option == 2):
      continue
      
    elif(option == 3):
      start = int(input('Enter start of range: '))
      end = int(input('Enter start of range: '))
      newtuple = value[start:end]
      print(newtuple)
    elif(option == 4):
      templist = list(value)
      templist.append(100)
      value = tuple(templist)
      print(value)
    elif(option == 5):
      templist = list(value)
      templist = sorted(value)# reverse = True (descending)
      value = tuple(templist)
      print(value)
