


class Person():
    def __init__(self, age, thalach):
        self.age = age
        self.thalach = thalach
    
    def test(self):
        return self.age

    def info():
        self.input = input("Would you like some info on prevention of heart disease or to keep diseases from getting worse?")
        while self.input == yes or self.input == Yes:
            #make lists of the info and then print random
            print("If you are smoking it is recommended that you stop, as nicotine can narrow your blood vessels which is not good.")
            self.input = input("Would you like more information?")




person_1 = Person(19, 7787)
print(person_1.test())








