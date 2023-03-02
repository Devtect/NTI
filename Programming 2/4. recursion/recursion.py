'''
recursion is a function that calls itself from within
recursion helps to visualize a complex problem into steps,
which can be solved more easily(iteratively  and recursively)
'''


# ITERATIVE (fast - complex)
def walk (steps):
    for step in range(1, steps + 1):
        print(f"You take step {step}")


# RECURSIVE (slower - simpler)
def walk (steps):
    if steps == 0:  # base condition/when do we stop
        return 
    walk(steps - 1)
    print(f"You take step {steps}")


walk(100)

# There is limit to how many frames can be added to the stack. Try 'walk(1000)'