""" Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, 
устанавливает порядковый номер. Код для проверки правильности решения: """


class Meta(type):
    
    #class_number = 0
        
    def __new__(cls, name, bases, dict):
        
        cls.class_number = 0
        return super().__new__(cls, name, bases, dict)

    def __init__(cls, *args, **kwargs):
        cls.class_number += 1
       
    #def __call__(cls, *args, **kwargs):
        #cls.class_number += 1
        #return super().__call__(*args, **kwargs)


        

Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

# Cls1.class_number == 0,  Cls2.class_number == 1

#print("Cls1.class_number = ", Cls1.class_number)

#print("Cls2.class_number = ", Cls2.class_number)

#assert (Cls1.class_number, Cls2.class_number) == (0, 1) #should be True

a, b = Cls1(''), Cls2('')

#a.class_number == 0, # b.class_number == 1, 

print("a.class_number = ", a.class_number)
print("b.class_number = ", b.class_number)
#assert (a.class_number, b.class_number) == (0, 1)   #should be True