#Задача 2: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

threeDigitNumber = int(input("Imput three digit number  "))
firstDigit = threeDigitNumber//100
secondDigit = threeDigitNumber//10%10
thirdDigit = threeDigitNumber%10
sum = firstDigit+secondDigit+thirdDigit
print ("the sum of the digit in your number is", sum) 