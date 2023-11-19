def global_interpolation(x_values, y_values, x):
    """
    Выполняет интерполяцию многочленом Лагранжа.

    :param x_values: Список значений x (узлов интерполяции).
    :param y_values: Список значений y (значений функции в узлах интерполяции).
    :param x: Точка, в которой производится интерполяция.
    :return: Значение интерполянта в точке x.
    """
    result = 0.0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

