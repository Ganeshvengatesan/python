########## Implementation of while-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING WHILE-LOOP") 
print("========================================") 
list1=[12,'JAMES',60,70,'PASS'] 
i=1 
while i<len(list1): 
  print(list1[i],end="  ") 
  i+=1 
print() 
 
########## Implementation of entry-level while-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING ENTRY-LEVEL WHILE-LOOP") 
print("====================================================") 
i=1 
while True: 
  if i>=len(list1): 
     break 
  print(list1[i],end="  ") 
  i+=1 
print() 
 
########## Implementation of middle-level while-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING MIDDLE-LEVEL WHILE-LOOP") 
print("=====================================================") 
i=0 
while True: 
  i+=1 
  if i>=len(list1): 
     break  
  print(list1[i],end="  ") 
print() 
 
########## Implementation of exit-level while-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING EXIT-LEVEL WHILE-LOOP") 
print("===================================================") 
i=1 
while True: 
  print(list1[i],end="  ") 
  i+=1 
  if i>=len(list1): 
     break  
print() 
 
 
 
 
########## Implementation of while-else-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING WHILE-ELSE-LOOP") 
print("==============================================") 
i=1 
while i<len(list1): 
  print(list1[i],end="  ") 
  i+=1 
else: 
  print("The loop is ended") 
print() 
 
########## Implementation of for-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING FOR-LOOP") 
print("=======================================") 
for i in range(1,len(list1)): 
  print(list1[i],end="  ") 
print() 
 
########## Implementation of for-else-loop ####### 
 
print("ACCESSING LIST ELEMENTS USING FOR-ELSE-LOOP") 
print("===========================================") 
for i in range(1,len(list1)): 
  print(list1[i],end="  ") 
else: 
  print("The loop is ended") 
print() 
 
########## Implementation of for-loop (for each) ####### 
 
print("ACCESSING LIST ELEMENTS USING FOR-LOOP (FOR EACH)") 
print("==================================================") 
for item in list1: 
  print(item,end="  ") 
print() 
