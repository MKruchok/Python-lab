import os
class Couch:
    best_couch = "Laura"
    @staticmethod
    def best__couch():
        return Couch.best_couch

    def __init__(self, name="Not specified", material="Not specified", in_stock="No", width: float=0, height: float=0, color="Not specified", brand="Not specified") :
        self._name = name
        self._material = material
        self._in_stock = in_stock
        self._width = width
        self._height = height
        self._color = color
        self._brand = brand

    def __del__(self):
        print(os.linesep+ "Object deleted.")

    def __str__(self):
        value = ("Name: "+self._name+ "\nMaterial: "+self._material+ "\nIn_stock: "+self._in_stock+ "\nWidth: "+str(self._width) +"\nHeigh: "+str(self._height)+ "\nColor: "+self._color+ "\nBrand: "+self._brand+ os.linesep)
        return value

def main():
    obj1 = Couch("Laura","Pirano","Yes",250,85,"white","Claudia")
    print(obj1.__str__())

    obj2 = Couch("Alonzo","Praktic","No",210,75,"black")
    print(obj2.__str__())

    obj3 = Couch("Leonardo","Fibril","Yes",160,80)
    print(obj3.__str__())

    print(f"\nBest couch: {obj1.best__couch()}")

if 1:
    main()
