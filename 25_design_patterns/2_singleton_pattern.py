# what is a design pattern (google, refactorguru)
# what is singleton (google)

class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is singleton, Already have an instance')
        pass
    
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance    
    
first = Singleton.get_instance()
print(first)