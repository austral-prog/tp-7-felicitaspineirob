def index_of_by_index(word, list, index):
    if not word in list[index:]: return -1
    
    for i, e in enumerate(list[index:]):
        if word == e:
            return i + len(list[:index])


def index_of_empty(list):
    if not "" in list: return -1
    for i, e in enumerate(list):
        if e == "":
            break
    return i

        
def index_of(word, list):
    
    if not word in list: return -1
    for i, e in enumerate(list):
        if e == word:
            break
    return i
    

#colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
def put(word, list):
    if not "" in list: return -1 
    for i, e in enumerate(list): 
        if e == "": 
            break
    list[i] = word 
    return i #returnea la index
    


def remove(word, list):
    if not word in list: return 0 # si la word no esta en list directo te pone 0
    count = 0 
    for i, e in enumerate(list): 
        if e == word:
            list[i], count = "", count +1 
    return count
