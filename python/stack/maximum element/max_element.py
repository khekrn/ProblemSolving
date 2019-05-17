class CustomStack:
    def __init__(self):
        self.stack = []
        self.res = 0

    def push(self, item):
        self.stack.append(item)
        self.res += item
    
    def pop(self):
        item = self.stack.pop()
        self.res -= item
    
    def print_sum(self):
        print(self.res)

    def __str__(self):
        return str(self.stack)

def main():
    stack = CustomStack()
    N = int(input())
     
    for _ in range(N):
        unknown = input()
         
        command = unknown[0]
         
        if command == '1':
            cmd, value = map(int, unknown.split())
            stack.push(value)
        elif command == '2':
            stack.pop()
        else:
            stack.print_sum()
     
 
 
if __name__ == '__main__':
    main()