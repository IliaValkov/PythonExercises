'''
The Abstraction chapter goes one about, how to create 
function in order to hide explicit implmentations and to 
create reusable code blocks. There are different ways in which to
pass parameters and keyword parameters to the functions. Woth 
noting is the use of the * and the ** when passing parameters
or defining a function.
'''

# Closures 
'''
A closure is a function that stores it's enclosing scopes. An
example for such a functino follows. 
'''

def multiplier(factor): 
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor 

double = multiplier(2)

print(double(9))

# Recursion in Python