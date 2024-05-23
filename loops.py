def index_of_by_index(word, list, index):
    i=0
    while i < len(my_list):
        if my_list(i)==word:
            return i
        i+=1
    return -1
    
def index_of_empty(list):
    i=0
    while i < len(list):
        if list[i]=="":
            return i
        i+=1
    return -1

def index_of(word, list):
    i=0
    while i < len(list):
        if list[i] == word:
            return i
        i+=1
    return -1


def put(word, list):
    i=0 
    count=0
    while i < len(list):
        if list[i]=="":
            list[i]=word
            return i 
        i+=1
    return -1


def remove(word, list):
    i=0
    count=0
    while i <len(list):
        if my list[i] ==word:
            list[i]=""
            count+=1
        i+=1
    return count
