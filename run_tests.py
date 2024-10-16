def q3():
    list1 = ["bluh", [1, 4, 7]]

    list2 = ["bluh",  list1[1]]  #Point A
    list2[0] += "bluhhhh"

    list2[1].append(6)
    list1[1] + [3]  #Point B
    list1[1] = list1[1] + [5]
    list2[1].append(8)  #Point C

    print(list1)
    print(list2)

class Value:
    """Stores a numeric value"""
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        self.previous_values = []

    def __str__(self) -> str:
        return f'{self.name}:{self.value} {self.previous_values}'

def multiply(value: Value, scale: int) -> Value:
    #scaledValue = copy.copy(value)
    scaledValue = copy.deepcopy(value)
    scaledValue.name = f'{value.name}_{scale}'
    scaledValue.value *= scale
    scaledValue.previous_values.append(value.value)

    return scaledValue


import copy



class Comedian:
    def __init__(self, joke):
        self.__joke = joke
    def change_joke(self, joke):
        self.__joke = joke
    def get_joke(self):
        return self.__joke
def process(c):
    c = copy.copy(c)
    c[1] = Comedian("joke3")
    c.append(Comedian("joke4"))
    c = c + [Comedian("joke5")]
    c[0].change_joke("joke6")


class Event():
    def __init__(self, start_time, end_time):
        assert(type(start_time) == int)
        assert(type(end_time) == int)
        if start_time >= end_time:
            raise ValueError
        self.start_time = start_time
        self.end_time = end_time
        
class Calendar:
    __events = []
    def __init__(self):
        global __events
        __events = []
    def get_events(self):
        global __events
        return __events
    def add_event(self,event):
        global __events
        if not isinstance(event, Event):
            raise TypeError
        else:
            __events.append(event)
            
            
class Joker:
    joke = "I dressed as a UDP packet at the party. Nobody got it."
    def change_joke(self):
        print(f'self.joke = {self.joke}')
        print(f'Joker.joke = {Joker.joke}')
        Joker.joke = "How does an OOP coder get wealthy? Inheritance."
        self.joke = "Why do Java coders wear glasses? They can't C#."
        print(f'self.joke = {self.joke}')
        print(f'Joker.joke = {Joker.joke}')
def main():
    j = Joker()
    print(f'j.joke = {j.joke}')
    print(f'Joker.joke = {Joker.joke}')
    j.change_joke()
    print(f'j.joke = {j.joke}')
    print(f'Joker.joke = {Joker.joke}')

if __name__ =="__main__":
    main()
