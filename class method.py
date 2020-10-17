class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height

    @classmethod
    def new_square(cls,side_length):
        return cls(side_length,side_length)
square=rectangle.new_square(5)
print(square.calculate_area())

#setter

class Pizza:
    def __init__(self,toppings):
        self.toppings=toppings
        self._pineapple_allowed=False
    @property
    def pineapple_allowed(self):
       return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        password=input("enter the password:")
        if password=="poisson":
            self._pineapple_allowed=value
            print("autorisation accordée")
        else:
            raise ValueError("alerte intrus !")
pizza=Pizza(["cheese,tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed=True
print(pizza.pineapple_allowed)



