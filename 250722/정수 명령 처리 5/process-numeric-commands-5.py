N = int(input())
ary = []

for _ in range(N):
    commands = input().split()
    cmd = commands[0]

    if cmd == 'push_back':
        ary.append(commands[1])
    elif cmd == 'pop_back':
        if ary:
            ary.pop()
    elif cmd == 'size':
        print(len(ary))
    elif cmd == 'get':
        index = int(commands[1]) - 1  
        if 0 <= index < len(ary):
            print(ary[index])
