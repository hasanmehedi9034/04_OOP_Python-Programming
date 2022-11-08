anagrams=(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
 
def strAnag(anagrams):
    dict = {}
   
    for i in anagrams:
        sort = str(sorted(i))
        if sort in dict:
            dict[sort].append(i)
        else:
            dict[sort] = [i]
    return dict
 
anagram = strAnag(anagrams)
print(list(anagram.values()))
