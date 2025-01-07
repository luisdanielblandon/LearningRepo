print("This program helps convert Fahrenheit to Celsius or vice versa\n")

ConversionSelection = input("Do you want to convert from F to C (type 'F') or from C to F (type 'C')\n")

if ConversionSelection == 'C':
      ConvertedTemp = (int(input("Please input the temperature in Celsius to be converted:\n")) * 9 / 5) + 32
      print("The temperature in Fahrenheit is ",ConvertedTemp)

if ConversionSelection == 'F':
      ConvertedTemp = (int(input("Please input the temperature in Fahrenheit to be converted:\n")) - 32) * 5 / 9
      print("The temperature in Celsius is ",ConvertedTemp)

if ConversionSelection != 'C' and ConversionSelection != 'F':
      print("You did not select a valid conversion type! Try again, dummy.")