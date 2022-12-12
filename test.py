class A:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def print(self):
        print(self.x, self.y)

def nums():
    return (10, 10)

a = A()

a.x, a.y = nums()

a.print()