'''
def sol(n):
    for i in range(n):
        print(''.join(map(str, range(1, n-i+1))))
sol(int(input()))
'''
def sol(n):
    result = ''
    temp = ''
    for i in range(1, n+1):
        temp += str(i)
        result = temp + '\n' + result
    print(result)
sol(int(input()))
