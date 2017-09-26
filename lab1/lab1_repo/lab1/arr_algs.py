def func1(x):
    m=x[1]
    for i in x:
        if i<m:
            m=i
    print(m)

func1([1,-6,78,0])

def func2(x):
    s=0;
    for i in x:
        s=s+i
    print(s/len(x))

func2([1,2,4,6])