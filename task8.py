#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
#отломить k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no
chocolateLength=int(input("Input the length of your chocolate bar"))
chocolateWidth=int(input("Input the width of your chocolate bar"))
sliceNumber=int(input("Input the number of slices"))
if sliceNumber//chocolateLength and sliceNumber//chocolateWidth:
    print("You can break off",sliceNumber,"from the bar of this size")
else:
    print("You can't break off",sliceNumber,"from the bar of this size")