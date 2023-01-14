from typing import Iterable

given_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten_list = []

def flatten (input_list):
    for element in input_list:
        if isinstance(element,(list,dict,set,tuple)):
    #OR if isinstance(element,Iterable) and isinstance(element,str) != True :
            flatten(element)
        else: 
            flatten_list.append(element)
    

flatten(given_list)

print(flatten_list)

#########################################################################

"""
Object : To reverse everything in a list and itself. 
"""
#given_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def reversing(input_list):
    input_list.reverse()
    print("REVERSED  : " , input_list)
    for element in input_list:
        if isinstance(element,Iterable) and isinstance(element,str) != True :
            reversing(element)
        else:
            pass
    return input_list

reversed_list = reversing(given_list)

print(reversed_list)





