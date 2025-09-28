import matplotlib.pyplot as plt
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def build_graph(a, b, f):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

# Original a and b values
a = 0  # Нижня межа
b = 2  # Верхня межа

if __name__ == "__main__":
    build_graph(a, b, f)

    # Monte Carlo Integration
    num_points = 100000

    # Define the bounding box for random points
    max_y = f(b)  # Since f(x) = x^2, max value is at b

    # Generate random x and y coordinates within the bounding box
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, max_y, num_points)

    # Count points under the curve
    points_under_curve = np.sum(random_y < f(random_x))

    # Calculate the area of the bounding box
    area_bounding_box = (b - a) * max_y

    # Estimate the integral
    monte_carlo_integral = (points_under_curve / num_points) * area_bounding_box

    print(f"\nMonte Carlo Integral Estimate: {monte_carlo_integral:.6f}")

    import scipy.integrate as spi

    # Analytical calculation with scipy.integrate.quad
    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Analytical Integral (quad) Estimate: {quad_result:.6f}")
    print(f"Absolute Error for quad: {quad_error:.6e}")

    # Conclusions
    print("\n--- Conclusions ---")
    print(f"Difference between Monte Carlo and Analytical: {abs(monte_carlo_integral - quad_result):.6f}")
    print("The Monte Carlo method provides an approximation of the integral. Its accuracy depends on the number of random points used. With a larger number of points (e.g., 100,000), the estimate gets closer to the true analytical value. The `scipy.integrate.quad` function provides a highly accurate (nearly exact) numerical integration result, which serves as a good benchmark for comparison.")
