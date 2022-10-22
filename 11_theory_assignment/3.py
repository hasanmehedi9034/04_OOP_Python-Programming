s = 'Programming Hero is the best'

def rev_word(s):
    split_string = s.split()
    
    for i, word in enumerate(split_string):
        split_string[i] = word[ : : - 1]
    
    return "".join(' ' + i for i in split_string)[1 : ]
        
print(rev_word(s))