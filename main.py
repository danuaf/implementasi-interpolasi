import numpy as np
import matplotlib.pyplot as plt
from polynom.polinomLangrange import polinomLangrange
from polynom.polinomNewton import polinomNewton


if __name__ == "__main__":
    # Data
    x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

    # Test interpolasi di rentang x dan membuat plot hasilnya
    x_values = np.linspace(5, 40, 100)
    y_lagrange = [polinomLangrange(x, y, xi).hitung() for xi in x_values]
    y_newton = [polinomNewton(x, y, xi).hitung() for xi in x_values]

    # mengkomparasi hasil antara kedua metode (akan ditampilkan pada terminal)
    key_points = [7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5]
    for kp in key_points:
        y_lag = polinomLangrange(x, y, kp).hitung()
        y_new = polinomNewton(x, y, kp).hitung()
        print(f"At x = {kp:.1f}, Lagrange = {y_lag:.4f}, Newton = {y_new:.4f}")


    fig, axs = plt.subplots(3, 1, figsize=(12, 12))

    # Plot untuk metode Lagrange 
    axs[0].plot(x, y, 'o', label='Data Points')
    axs[0].plot(x_values, y_lagrange, '-', color='red', label='Lagrange Interpolation')
    axs[0].set_xlabel('Tegangan, x (kg/mm^2)')
    axs[0].set_ylabel('Waktu patah, y (jam)')
    axs[0].set_title('Lagrange Interpolation')
    axs[0].legend()
    axs[0].grid(True)

    # Plot untuk metode Newton 
    axs[1].plot(x, y, 'o', label='Data Points')
    axs[1].plot(x_values, y_newton, '--', color='blue', label='Newton Interpolation')
    axs[1].set_xlabel('Tegangan, x (kg/mm^2)')
    axs[1].set_ylabel('Waktu patah, y (jam)')
    axs[1].set_title('Newton Interpolation')
    axs[1].legend()
    axs[1].grid(True)

    # Plot untuk metode Lagrange dan Newton
    axs[2].plot(x, y, 'o', label='Data Points')
    axs[2].plot(x_values, y_lagrange, '-', color='red', label='Lagrange Interpolation')
    axs[2].plot(x_values, y_newton, '--', color='blue', label='Newton Interpolation')
    axs[2].set_xlabel('Tegangan, x (kg/mm^2)')
    axs[2].set_ylabel('Waktu patah, y (jam)')
    axs[2].set_title('Newton Interpolation')
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4) 
    plt.show()
