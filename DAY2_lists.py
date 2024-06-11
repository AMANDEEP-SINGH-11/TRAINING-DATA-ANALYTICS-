#QUESTION 1
colors = ["red","blue", "green", "yellow"]
print( "FIRST ELEMENT : ", colors[0])
print("SECOND ELEMENT : ", colors[1])
print("THIRD ELEMENT : ", colors[2])
print("FOURTH ELEMENT : ", colors[3])
print("SECOND-TO-LAST ELEMENT : ", colors[-2]) 
print("SECOND AND THIRD ELEMENT : ", colors[1:3])
#print("ELEMENT AT INDEX 4 :" , colors[4])
#QUESTION 2
water_level=[730,709,682,712,733,751,740]
water_level.remove(682)
water_level.insert(2,693)
print(water_level)
#QUESTION 3
water_level.append(722)
print(water_level)
#QUESTION 4
water_level1 = [722,770,745]
water_level.extend(water_level1)
print(water_level)
#QUESTION 5 



#.....  TUPLE  .....
#1 CREATING A TUPLE 
colors = ('red' , 'green', 'blue' )
print(colors[1])


#2 WHY TUPLE ARE CONSIDERED IMMUTABLE :
#We can't change the elements of a tuple,
#but we can execute a variety of actions on them such
#as count, index, type, etc.
value = 'yellow'
print("Value to be added : ", value )
colors1 = (' yellow ' , )
colors2 = colors + colors1
print("updated tuple is : ", colors2)
#3 