# 17427_약수의_합_2.py           

if __name__ == '__main__':
    num = int(input())
    result = 0

    # g(N)
    for i in range (1, num+1):
        result += (num // i) * i
    
    print(result)