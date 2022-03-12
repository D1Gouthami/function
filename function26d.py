def fizzbuzz():
   a=int(input("enter the num"))
   if a%3==0:
        print('fizz')
   elif a%5==0:
        print("buzz")
   elif a%3==0 and a%5==0:
        print("fizzbuzz")
   else:
        print("nothing")
fizzbuzz()