names = ['Spider', 'Bat', 'Wonder wo']
prof = ['photographer', 'philantgropist', 'nurse']

# job = dict(zip(names, prof))
# print(job)

my_dict = {names[i] : prof[i] for i in range(len(names))}

my_dict = {
    (key + "man" if key != 'Spider' else 'Superman'):
    (value if value != 'photographer' else 'journalist') 
    for key, value in my_dict.items()
    }

# print(my_dict)

