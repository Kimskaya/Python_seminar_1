#Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
#Пример:*
#385916 -> yes
#123456 -> no
SixDigitNumber=int(input("Input your ticket number. Six digits only!  "))
FirstHalf=SixDigitNumber//1000
SecondHalf=SixDigitNumber%1000
firstDigit=FirstHalf//100
secondDigit=FirstHalf//10%10
thirdDigit=FirstHalf%10
forthDigit=SecondHalf//100
fifthDigit=SecondHalf//10%10
sixthDigit=SecondHalf%10
firstHalfSum=firstDigit+secondDigit+thirdDigit
secondHalfSum=forthDigit+fifthDigit+sixthDigit
if firstHalfSum==secondHalfSum:
    print("Your ticket is lucky, eat it")
else:
    print("Your ticket is not lucky, don't eat it")
