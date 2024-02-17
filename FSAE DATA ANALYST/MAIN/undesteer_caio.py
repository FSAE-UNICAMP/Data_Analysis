import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

# Leitura do arquivo CSV
def caio_analises1 (df, wheelbase, steer_ratio):

    # Cálculo de Neutral_Steer
    df['Neutral_Steer'] = wheelbase * steer_ratio * df['Lateral_G'] * 9.81 * 57.3 * 12.96 / df['Wheel_speed_reference']**2

    # Cálculo do Understeer_Angle
    df['Understeer_Angle'] = abs(df['STEERING']*(1/steer_ratio)) - abs(df['Neutral_Steer']/steer_ratio)

    # Plotar gráfico de Lateral_G pelo TIME
    plt.figure(figsize=(12, 9))

    max_lateralg_channel = np.max(df['Lateral_G'])
    min_lateralg_channel = np.min(df['Lateral_G'])

    df['STEERING_abs'] = abs(df['STEERING'])
    df['Neutral_Steer_abs'] = abs(df['Neutral_Steer'])

    # Calcula as derivadas dos valores
    steering_derivative = np.gradient(df['STEERING_abs'], df['TIME'])
    neutral_steer_derivative = np.gradient(df['Neutral_Steer_abs'], df['TIME'])
    # Calcula as derivadas dos valores absolutos
    abs_steering_derivative = abs(steering_derivative)
    abs_neutral_steer_derivative = abs(neutral_steer_derivative)
    # Calcule a média das derivadas dos valores absolutos
    mean_steering_derivative = np.mean(abs_steering_derivative)
    mean_neutral_steer_derivative = np.mean(abs_neutral_steer_derivative)

    max_steering_derivative = np.max(steering_derivative)
    max_neutral_steer_derivative = np.max(neutral_steer_derivative)

    min_steering_derivative = np.min(steering_derivative)
    min_neutral_steer_derivative = np.min(neutral_steer_derivative)

    # Gráfico de Lateral_G
    plt.subplot(4, 1, 1)
    plt.plot(df['TIME'], df['Lateral_G'], label=f'Lateral Acceleration | Max= {max_lateralg_channel:.2f} G | Min= {min_lateralg_channel:.2f} G', color='purple')
    plt.title('Lateral Acceleration Channel')
    plt.xlabel('')
    plt.ylabel('Lateral Acceleration (G)')
    plt.legend()

    # Calcular e adicionar integral no gráfico
    integral_steering = simps(abs(df['STEERING']), df['TIME'])
    integral_neutral_steer = simps(abs(df['Neutral_Steer']), df['TIME'])

    # Gráfico de STEERING e Neutral_Steer
    plt.subplot(4, 1, 2)
    plt.plot(df['TIME'], df['STEERING'], label=f'Real Steering | Integral KPI (Total Sum)= {integral_steering:.2f} ', color='blue')
    plt.plot(df['TIME'], df['Neutral_Steer'], label=f'Neutral Steer | Integral KPI (Total Sum)= {integral_neutral_steer:.2f} ', color='red')
    plt.title('Real Steering & Neutral Steer Channel')
    plt.xlabel('')
    plt.ylabel('Steering Angle (°)')
    plt.legend()

    mean_understeer_channel = np.mean(df['Understeer_Angle'])
    max_understeer_channel = np.max(df['Understeer_Angle'])
    min_understeer_channel = np.min(df['Understeer_Angle'])

    # Gráfico de Understeer_Angle
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

    plt.tight_layout()
    # Ajuste a disposição dos subplots para evitar sobreposição com mais espaçamento
    plt.subplots_adjust(left=0.076)
    plt.subplots_adjust(bottom=0.052)
    plt.subplots_adjust(right=0.987)
    plt.subplots_adjust(top=0.974)
    plt.subplots_adjust(wspace=0.2)
    plt.subplots_adjust(hspace=0.28)

    plt.show()