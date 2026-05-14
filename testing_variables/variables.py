import os
from get_data.fetch_data import load_heart_data
import matplotlib.pyplot as plt
import seaborn as sns

#function to make plots
def make_plot(variable_1, variable_2):
    variable_1_label = variable_1.replace('_', ' ')
    variable_2_label = variable_2.replace('_', ' ')

    df, target_name = load_heart_data()

    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x=variable_1,
        y=variable_2,
        hue=target_name,
        style=target_name,
        s=90
    )

    plt.title(f'Heart Disease: {variable_1_label} vs {variable_2_label}')
    plt.xlabel(f'{variable_1_label}')
    plt.ylabel(f'{variable_2_label}')
    plt.legend(title='Heart Disease')
    plt.grid(True)
    plt.savefig(f'/workspaces/Final_Coding_Project/plots/{variable_1_label}vs{variable_2_label}.png', dpi=150)
    plt.close()


# make_plot('age', 'trestbps')
# make_plot('trestbps', 'thalach')
# make_plot('oldpeak', 'thalach')
# make_plot('chol', 'trestbps')
# make_plot('chol', 'oldpeak')
# make_plot('chol', 'thalach')
# make_plot('chol', 'age')
# make_plot('oldpeak', 'age')
# make_plot('age', 'thalach') prob best one yet
