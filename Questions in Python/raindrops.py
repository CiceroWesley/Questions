def convert(number):
    if number % 3 == 0:
      print("Pling",end="")
    if number % 5 == 0:
      print("Plang",end="")
    if number % 7 == 0:
      print("Plong",end="")    
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
      print(number) 

numberinput= int(input("Number:"))        
convert(numberinput)

'''
Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if a one number is a factor of another is to use the [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation).

The rules of `raindrops` are that if a given number:

- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- _does not_ have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
'''