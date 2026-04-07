from ucimlrepo import fetch_ucirepo 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_heart_data():
    #copied directly from UCI Machine Learning Repository package documentation 
    # fetch dataset 
    heart_disease = fetch_ucirepo(id=45) 
  
    # data (as pandas dataframes) 
    X = heart_disease.data.features 
    y = heart_disease.data.targets 
  
# metadata 
print(heart_disease.metadata) 
  
# variable information 
print(heart_disease.variables) 