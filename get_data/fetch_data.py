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
  
    feature_names = heart_disease.variables[heart_disease.variables['role'] == 'Feature']['name'].tolist()
    target_name = heart_disease.variables[heart_disease.variables['role'] == 'Target']['name'].values[0]

    df = pd.DataFrame(heart_disease.data.features, columns=feature_names)
    df[target_name] = heart_disease.data.targets

    # print(df.head())

    return df, target_name

load_heart_data()