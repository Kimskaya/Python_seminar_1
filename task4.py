#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
#если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10
totalNumberOfCranes = int(input("input the number of cranes that was made by children. Mind that the number should be a multiple of 6  "))
if totalNumberOfCranes//6:
    PeteAndSergNumber = totalNumberOfCranes//6
    KateNumber = (PeteAndSergNumber+PeteAndSergNumber)*2
 
    print ("Pete made",PeteAndSergNumber,"cranes, Serg made",PeteAndSergNumber," and Kate made",KateNumber, "cranes")
else:
    print("you have imput the wrong number. Check if it is a multiple of 6")
