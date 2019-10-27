##### Factorials #####

##### Method 1 : Loops #####

def factorial_loops (num) :
    
    i = num - 1
    
    while i != 0 :
        num = num * i
        i -= 1
        
    
    return num

print(factorial_loops(3))
print(factorial_loops(4))
print(f"Factorial loops equals : {factorial_loops(5)}")

##### Method 2 : Recurssion #####

def factorial_recurssion (num) :
    if num == 1 :
        return num
    else :
        return num * factorial_recurssion(num - 1)
    

print(f"Factorial recurssion equals : {factorial_recurssion(5)}")


##### Fibonacci #####


##### Method 1: Loops #####

def fibonacci_loops (index) :
    
    index_length = index + 1
    count = 1
    start_result = 0
    end_result = 1
    
    while count != index_length :
        result = start_result + end_result
        start_result = end_result
        end_result = result
        
        count += 1
        
    return result

print(f"Fibonacci results is : {fibonacci_loops(4)}")
    
##### Method 2: Loops #####

    
def fibonacci_recurssion(num, start_result, end_result) :
    count = num
    
    if count == 1 :
        
        return end_result
    else :
        result = start_result + end_result
        start_result = end_result
        end_result = result
        return fibonacci_recurssion(num - 1, start_result, end_result)
    

        
print(f"Fibonacci recursion results is : {fibonacci_recurssion(4, 1, 1)}")
        

def fibonacci_elegant_recurssion(num) :
    if num == 0 :
        return 1
    elif num == 1 :
        return 1
    else :
        return fibonacci_elegant_recurssion(num - 1) + fibonacci_elegant_recurssion(num - 2)
        
print(f"Elegant method for fibonacci recurssion is : {fibonacci_elegant_recurssion(4)}")