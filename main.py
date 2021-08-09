'''
For in Loop
'''

#students = ['Bob', 'Adriana', 'Felix']

#for stu in students:
   #print('hi', stu)

   #For every instant in students , say hi

   #=====================================
#print(range(10))
#print(list(range(10)))
#print(list(range(3, 6)))
#print(list(range(3, 12, 3)))

#=====================================

#for x in range(6):
   #print(x + 1)
   #You can also change it multiplication, a range also starts from zero by default always remeber that


#for i in range (1, 6):
   #for j in range(i):
     #print( "*", end=" ")
     #print()


     #=====================================#
'''
While Loop
'''

#i = 1
#while i <10:
   #print(i)
   #i += 1
#It will keep runnin until out of memory

 #=====================================#
 #break statements

 #i = 1
 #while i < 10:
   #print(i)
   #if i == 3:
     #break
     #i += 1
#Breaks out of your while loop and stops
     #=====================================#

#contnue statements

#i = 1
#while i < 5:
   #i += 1
   #if i == 4:
     #continue
     #print(i)
#=====================================#

for i in range(1, 10):
  if i == 3:
    break
    print(i)