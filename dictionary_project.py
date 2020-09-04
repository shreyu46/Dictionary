import json
from difflib import get_close_matches
data=json.load(open(r"C:\Users\RAHUL\Desktop\python udemy course 1\data_dictionary.json"))

def find(name):
    n=name.lower()
    if n in data:
        return(data[n])
    elif n.capitalize() in data:
        return(data[n.capitalize()])
    elif n.upper() in data:
        return(data[n.upper()])
    else:
        #print("invalid")
        print("close matches to this are")
        x=get_close_matches(n,data)
        print(x)
        next_name=input("enter the word from close matches which matches your preferences\n")
        if next_name in x:
            return(data[next_name])
name=input("enter the word to find the meaning\n")
result=find(name)
if type(result)==list:
    for item in result:
        print(item)
else:
    print(result)