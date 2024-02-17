import matplotlib.pyplot as plt
import pandas as pd

def Undesteer(df):
    plt.subplot(4, 1, 3)
    plt.plot(df['TIME'], df['Understeer_Angle'], label=f'Understeer Angle | KPI Value (Avg) = {mean_understeer_channel:.2f} | Max= {max_understeer_channel:.2f} | Min= {min_understeer_channel:.2f}  ', color='green')
    plt.title('Understeer Angle Channel')
    plt.xlabel('')
    plt.ylabel('Understeer Angle (°)')
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(df['TIME'], steering_derivative, label=f'Steering Agressiveness | KPI Value (Avg)= {mean_steering_derivative:.2f} | Max= {max_steering_derivative:.2f} | Min = {min_steering_derivative:.2f} ', color='brown')
    plt.plot(df['TIME'], neutral_steer_derivative, label=f'Neutral Steer Agressiveness | KPI Value KPI (Avg)= {mean_neutral_steer_derivative:.2f} | Max= {max_neutral_steer_derivative:.2f} | Min = {min_neutral_steer_derivative:.2f}', color='orange')
    plt.title('Real Steering & Neutral Steer Agressiveness')
    plt.xlabel('TIME')
    plt.ylabel('Steering Agressiveness (°/s)')
    plt.legend()

df = pd.read_csv("teste.csv")
Undesteer(df)