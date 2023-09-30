def argsEx(*args) :
    for arg in args :
        print(arg);


# argsEx(4, 'Hello', 3 , 'Nothing');

def kwargsEx(**kwargs) :
    for (key,value) in kwargs.items() :
        print(f'key is {key} and value is {value}');

kwargsEx(title = 'Hello', age = 45, marks = 90, prof = 'Student');
