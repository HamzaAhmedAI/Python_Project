class Counter():
    object_count = 0

    def __init__(self):
        Counter.object_count += 1
    
    @classmethod
    def dispplay_count(cls):
        print("Total number of objects:", cls.object_count)

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.dispplay_count()