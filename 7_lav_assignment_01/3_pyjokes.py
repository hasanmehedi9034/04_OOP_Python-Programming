import pyjokes

keywords = ['yes', 'jokes', 'tell', 'joke']

def tell_some_jokes():
    return pyjokes.get_joke()

def listen():
    return input("Say something : ")

def talkback(response):
    print(response)

while True:
    command = listen().lower()

    broken_words = command.split()

    for word in broken_words:
        if word in keywords:
            print(f'Jokes : "{tell_some_jokes()}"')
        else:
            talkback('do you listen joke?')
        