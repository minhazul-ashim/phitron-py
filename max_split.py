str = input();

def maxSplit() :
    target = 0;
    curr = 0;
    idx = 0;
    count = 0;
    strs = [];
    for i in range(0, str.__len__()) :
        if(i == 0) :
            curr += 1;
            continue;
        
        if(target == curr) :
            strs.append(str[idx : i]);
            idx = i;
            count += 1;
            curr = 0;
            continue;

        if(str[i] == str[i-1]) :
            curr+=1;
        else :
            target = curr;
            curr = 1;
    
        if(target == curr) :
            strs.append(str[idx : i+1]);
            idx = i+1;
            count += 1;
            curr = 0;
            continue;

    print(count);
    for x in strs :
        print(x);

maxSplit();
