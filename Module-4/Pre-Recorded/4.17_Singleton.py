# Only creats One Instance of a Class


class Singleton:
    _instance = None                # Class variable

    def __new__(cls):                                                    # 'new' is a built-in method; whenever an Object is creaed 'new' is called

        if cls._instance is None:                                             # If there is no Object created, then create an Object
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance                                                  # If there is an Object, just return it



obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)                     # returns a Boolean