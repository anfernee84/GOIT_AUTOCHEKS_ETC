"""
Напишите классы сериализации контейнеров с данными Python в json, bin файлы. Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface.
"""

from abc import ABCMeta, abstractmethod
import json
import pickle

class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
    
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass

class JsonSerDeser(SerializationInterface):
    def __init__(self, filename, data):
        super(JsonSerDeser, self).__init__(filename, data)
    
    def serialize(self):
        with open(self.filename, 'w') as fh:
            json.dump(self.data, fh)
    
    def deserialize(self):
        with open(self.filename, 'r') as fh:
            return json.load(fh)

class BinSerDeser(SerializationInterface):
    def __init__(self, filename, data):
        super(BinSerDeser, self).__init__(filename, data)

    def serialize(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self.data, fh)
    
    def deserialize(self):
        with open(self.filename, 'rb') as fh:
            return pickle.load(fh)

j = JsonSerDeser("123.json", {"1":"one", "2":"two"})
j.serialize()
print (j.deserialize())

b = BinSerDeser("123.bin", {"1":"oneee", "2":"twooo"})
b.serialize()
print(b.deserialize())



"""
Напишите класс метакласс Meta, который всем классам для кого он будет метаклассом устанавливает порядковый номер. 
"""

class Meta(type):
    children_number = 0
    def __new__(mcs, name, bases, attrs):
        attrs['class_number'] = Meta.children_number
        mcs.children_number += 1
        return type.__new__(mcs, name, bases, attrs)

Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
print(Cls1.class_number)
print(Cls2.class_number)


