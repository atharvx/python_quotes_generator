'''Atharv Project to Generate the Quotes based on category'''


import json  
with open('quotes.json', encoding="utf-8") as file:  
    data = json.load(file)  
tag = input('Enter a tag:')  
dictionary = {}  
for quote in data:  
    if tag in quote["category"]:  
        dictionary[quote["author"]]=quote["quote"]  
if(len(dictionary)==0):  
    print("Sorry, we couldn't find any quote with given tag")  
else:  
    keys = list(dictionary.keys())  
    keys.sort(reverse=True)  
    sorted_dict = {i: dictionary[i] for i in keys}  
    for i in sorted_dict:  
        print("Popularity: ", i)  
        print("Quote: ",sorted_dict[i])  
        print()  
        a = input("Next(Y/N):")  
        print()  
        if(a=="Y"):  
            continue
        else:  
            break 