"""
1. input/output
2. process/decide
3. output/talkback

"""
greet_words = ['hi', 'hello', 'yo', 'hey']
bye_words = ['bye', 'tata', 'hasta la vista']
bad_words = ['dog', 'pocha']

def listen():
    return input("Say something: ")

def decide(command):
    command = command.lower()
    broken_words = command.split(" ")

    for word in broken_words:
        if word in greet_words:
            talkback('Hello Man')
            break

        elif word in bye_words:
            talkback('bye bye')
            break

        elif word in bad_words:
            talkback('Your are bad guy')

    
def talkback(response):
    print(response)

while(True):
    command = listen()
    decide(command)