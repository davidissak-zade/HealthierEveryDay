import matplotlib.pyplot as plt
import numpy
import json

def plot_progress(USER_TOKEN):
    with open("DB.json", "r") as fp:
        data = json.load(fp)
    BMI_history = data[USER_TOKEN]["BMI_history"]
    userName = data[USER_TOKEN]["name"]
    BMI_rates = []
    time = []
    for i in range(len(BMI_history)):
        time.append(i+1)
        BMI_rates.append(BMI_history[i])

    plt.plot(time, BMI_history)
    plt.ylabel(userName + "'s BMI rate (bmi)")
    plt.xlabel("Days after first check up")
    plt.show()