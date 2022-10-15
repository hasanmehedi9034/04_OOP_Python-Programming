a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string(s):
    s = s.replace(',', "")
    s = s.replace('.', "")

    split_string = s.split()
    print(split_string)

    out_put = ""

    for i in a:
        for j in range(len(split_string) - 1, -1, -1):
            if i.lower() == split_string[j].lower():
                out_put += split_string[j + 1] + " "
                break

    return out_put.rstrip(out_put[-1])


output = create_new_string(s)

with open('out.txt', 'w') as f:
    f.write(output)