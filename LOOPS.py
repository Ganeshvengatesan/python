######## Implementation of if-else block ####### 

print("CHECKING WHETHER THE GIVEN INTEGER IS ODD OR EVEN") 
print("=================================================") 
n=int(input("Enter an integer : ")) 
if n%2==0: 
  print(n,"  is even") 
else: 
  print(n,"  is odd") 

############## Implementation of nested-if ######

  print("FINDING THE GREATEST AMONG THREE VARIABLES") 
print("==========================================") 
a=int(input("enter a : ")) 
b=int(input("enter b : ")) 
c=int(input("enter c : ")) 
if (a>b): 
  if (a>c): 
     print("a is big") 
  else: 
     print("c is big") 
else: 
   if (b>c): 
     print("b is big") 
   else: 
     print("c is big")


############## Implementation of if-elif-else  ######### 
 
print("FINDING THE CORRESPONDING DAY OF THE GIVEN INTEGER") 
print("==================================================") 
day=int(input("Enter an integer 1-7 : ")) 
if (day==1): 
   print(day," - SUNDAY") 
elif (day==2): 
   print(day," - MONDAY") 
elif (day==3): 
   print(day," - TUESDAY") 
elif (day==4): 
   print(day," - WEDNESDAY") 
elif (day==5): 
   print(day," - THURSDAY") 
elif (day==6): 
   print(day," - FRIDAY") 
elif (day==7): 
   print(day," - SATURDAY") 
else: 
   print("Wrong input, please enter an integer in the range 1-7")
