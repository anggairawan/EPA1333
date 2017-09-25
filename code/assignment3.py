#%%
"""
Assignment 3.1
Write a function removeConsecutiveElements that takes a list as input and returns a list where all consecutive elements 
are reduced to a single element, so removeConsecutiveElements([1, 2, 2, 2, 3]) returns the list [1, 2, 3].
"""

# Your code goes here
def removeConsecutiveElementsSet(l):
    """
    remove the duplicate of the element on the list
    input: list
    output: list
    """
    
    set_of_list = set(l)
    removed_list = list(set_of_list)
    return removed_list

def removeConsecutiveElements(l):
    """
    remove the duplicate of the element on the list
    input: list
    output: list
    """
    removed_list = []
    
    for el in l:
        if el not in removed_list:
            removed_list.append(el)
    
    return removed_list

#if __name__ == "__main__":
lin = ['asd','asd','ads']
rem_list = removeConsecutiveElements(lin)
print(rem_list)
rem_list = removeConsecutiveElementsSet(lin)
print(rem_list)    
#%%
"""
Write a function front_x that takes a list of strings as input and returns a list with the strings in sorted order, 
except group all the strings that begin with 'x' first, so front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) 
returns ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
"""

# Your code goes here
def front_x(list_of_str):
    """
    sort the element of the list, except if it is started with 'x'
    """
    
    x_str = []
    non_x_str = []
    
    for string in list_of_str:
        if string[0] == 'x':
            x_str.append(string)
        else:
            non_x_str.append(string)
            
    x_str.sort()
    non_x_str.sort()
    
    x_str.extend(non_x_str)
    return x_str        
#%%    
ls = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark','asd']    
print(front_x(ls))   

#%%
"""
Write a function zipper that takes two lists as input, and return 
a list with the elements of both lists interchanged (like a zipper). 
For example, zipper(['a1','a2','a3','a4'],['b1','b2',' ']) should return ['a1', 'b1', 'a2', 'b2', 'a3', ' ', 'a3'].
Make sure in your solution that the function accepts lists of different lenghts as input and that either of the input 
lists can be the empty list.
"""

def zipper(l1,l2):
    lout = []
    
    if not l1 and not l2:
        return lout
    elif not l1:
        return l2
    elif not l2:
        return l1
        
    for i in range(min(len(l1),len(l2))):
        lout.append(l1[i])
        lout.append(l2[i])
    
    i += 1
    
    if len(l1) < len(l2):
        lout.extend(l2[i:])
    elif len(l1) > len(l2):
        lout.extend(l1[i:])
        
    return lout
    
#%%

l1 = ['a1','a2','asd','a4','asd']
l2 = ['b1','b2',' ','kll']

print(zipper(l1,l2))