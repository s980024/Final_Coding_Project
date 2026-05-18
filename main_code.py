import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from get_data.fetch_data import load_heart_data
from machine_learning.testing_KNN_model import KNN_model

class Person():
    def __init__(self, age, thalach):
        self.age = age
        self.thalach = thalach
    
    def run_KNN_model(self):
        print("This code will predict whether if you have heart disease on a scale of 0 to 4. O means you do not have heart disease and 1-4 are the varying degrees of heart disease, 4 being the worst. It will also show you the accuracy and the confusion matrix of the model. ")
        KNN_model(self.age, self.thalach)
        return self.age

    def info(self):
        self.input = input("Would you like some info on prevention of heart disease or to keep diseases from getting worse? ")
        self.list_info = ["If you are smoking it is recommended that you stop, as nicotine can narrow your blood vessels which is not good.", "It is recommended to change your diet to a low soidum/low fat diet and manage your weight.", "If you have not seen a doctor yet and your prediction says you have heart disease, it would be a good idea to schedule a doctor appointment.", "It is recommended to aim for at least of 150 minutes of moderate intensity of exercise once a week to try and keep it from getting worse.", "If you have a doctor and are on medications, it is recommended that you keep taking that medication until your doctor tells you not to.", "It is also good to get between 7-8 hours of sleep to help keep blood pressure low. "]
        self.i = 0
        if self.input == "yes" or self.input == "Yes":
            while self.i < len(self.list_info):
                #make lists of the info and then print random
                print(self.list_info[self.i])
                self.list_info.pop(self.i)
                self.i += 1
                input_break = input("Would you like more information? ")
                if self.i == len(self.list_info):
                    print("That is all the information I have for you.")
                    break
                elif input_break == "no" or input_break == "No":
                    break



age_input = input("What is your age? ")
thalach_input = input("What is your maximum heart rate achieved? ")
person_1 = Person(age_input, thalach_input)
print(person_1.run_KNN_model())
person_1.info()








