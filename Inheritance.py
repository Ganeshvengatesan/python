######### Compile time polymorphism #### 
class Addition: 
    def add(self, a, b): 
        return a + b         
 
print("Compile time polymorphism") 
print("====================") 
# Create object 
t1 = Addition() 
# Using integer arguments 
print(t1.add(4,5)) 
# Using string arguments 
print(t1.add("computer ","science"))  
# Using list arguments  
print(t1.add([12,'Williams'],[60,70,'pass']))       
 
######### Run time polymorphism #### 
class Fruit: 
    def color(self): 
        return "Fruits have generally some natural color" 
 
class Apple(Fruit): 
    def color(self): 
        return "Apple is Red in color" 
 
class Mango(Fruit): 
    def color(self): 
        return "Mango is Yellow in color" 
class Watermelon(Fruit): 
    def color(self): 
        return "Watermelon is Green in color" 
 
print("Run time polymorphism") 
print("=================") 
print(Apple().color()) 
print(Mango().color()) 
print(Watermelon().color()) 
print(Fruit().color())
