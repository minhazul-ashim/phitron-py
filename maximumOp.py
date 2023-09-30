n = int(input());
a = list(map(int, input().split()))

def maximize() :
    count = 0;
    
    for i in range(0, n) :

        if(a[i] % 2 != 0):
            break;

        if(a[i] % 2 == 0 and i < n-1) :
            a[i] = a[i] // 2;
        elif(a[i] % 2 == 0 and i == n-1) :
            a[i] = a[i] // 2;
            count += 1;
    
    return count;


print(maximize());