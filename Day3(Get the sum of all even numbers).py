
def get_sum_evenNum(lst):
    sum=0
    for i in lst:
        if i%2==0:
            sum+=i  
    return sum          

list=[2,1,4,5,6,7,10]
print(get_sum_evenNum(list))
