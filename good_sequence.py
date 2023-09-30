n = int(input());
a = list(map(int, input().split()))
b = [];
count = 0;

for i in range(0, 10**5) :
    b.insert(i, 0);

def goodSqns() : 
    global count;
    global n;
    if(n == 1 and b[n] == 0) :
        print(1);
        return;
    for num in a :
        b[num] += 1;

    for i in range(0, 10**5) :
        if(b[i] > i) :
            count += b[i] - i;
        elif(i > b[i]) :
            count += b[i];
    
    print(count);

goodSqns();



