import random
# A tuple is used to represent the chess board state.
# If the element of index 0 equals to 3, this means,
# that the 1 row has a queen on the 4th column

def conflict(state, nextX):
    nextY = len(state) 
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY - i):
            return True
    return False

def queens_base_case(num, state):
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1 :
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result 


state = (1,3,0)

print(f"Base case run: {list(queens_base_case(4,state))}")

print(f"Recursive function run, 4 queens: {list(queens(4))}")

def prettyprint(solution):
    print(solution)
    def line(pos, length=len(solution)):
        return ' . '*(pos) + ' X ' + ' . '*(length-pos-1)
    for pos in solution:
        print(line(pos))

prettyprint(random.choice(list(queens(8))))