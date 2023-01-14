from typing import Iterable


input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

for i in input_list:
    print(i,type(i),isinstance(i,Iterable))


input_list.reverse()

print(input_list)



