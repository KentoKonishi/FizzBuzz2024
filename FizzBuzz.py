num=input("数字を入力してください")

NUM=1
while NUM < int(num) :

 if 0 == NUM % 15 :
     print("Fizz Buzz")
 elif 0 == NUM % 5 :
     print("Buzz")
 elif 0 == NUM % 3:
     print("Fizz")
 else :
     print(NUM)

 NUM += 1