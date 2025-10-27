def add1(x,y,z): 
   return(x+y+z) 
def add2(x,y,z): 
   return(x+y+z) 
def add3(x,y,z=30): 
   return(x+y+z) 
def add4(*x): 
   sum=0 
   for i in x: 
     sum=sum+i 
   return(sum) 
def arithmetic(x,y): 
  a=x+y 
  b=x-y 
  c=x*y 
  d=x/y 
  return(a,b,c,d) 
print("Function") 
print("=======") 
print("Function with Required arguments") 
print("=========================") 
print("add1(100,200,300) : ",add1(100,200,300)) 
print("Function with keyword arguments") 
print("=========================") 
print("add2(y=15,z=20,x=40) : ",add2(y=15,z=20,x=40)) 
print("Function with default arguments") 
print("=======================") 
print("add3(y=150,x=200) : ",add3(y=150,x=200)) 
print("Function with variable length arguments") 
print("=============================") 
print("add4(10,20,30) : ",add4(10,20,30)) 
print("add4(10,20,30,40,50) : ",add4(10,20,30,40,50)) 
print("Function returning multiple values") 
print("=========================") 
print("arithmetic(10,20) : ",arithmetic(10,20))
