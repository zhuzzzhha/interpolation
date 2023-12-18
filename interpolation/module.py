def global_interpolation(x_values, y_values, x):
    """
    Выполняет интерполяцию многочленом Лагранжа.

    :param x_values: Список значений x (узлов интерполяции).
    :param y_values: Список значений y (значений функции в узлах интерполяции).
    :param x: Точка, в которой производится интерполяция.
    :return: Значение интерполянта в точке x.
    """
    if len(x_values) != len(y_values):
        raise ValueError("Длины x_values и y_values должны совпадать.")

    result = 0.0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

def find_two_nearest_points(x_values, x):

    """
    Находит ближайшую левую и ближайшую правую точки из массива x_values для x.

    :param x_values: Список значений сеточной функции.
    :param x: Точка, для которой надо найти ближайшие точки из x_values.
    :return: (l, l_val, r, r_val) - (индекс в x_values левой ближайшей точки, значение левой ближайшей точки, индекс в x_values правой ближайшей точки, значение правой ближайшей точки)
    """

    min_r_dist = float('inf')
    min_l_dist = float('inf')
    l_val = r_val = 0
    l = r = 0
    for i, x_i in enumerate(x_values):
        d = abs(x_i - x)
        if d < min_l_dist and x_i < x:
            l_val = x_i
            min_l_dist = d
            l = i
        elif d < min_r_dist and x_i > x:
            min_r_dist = d
            r_val = x_i
            r = i
    return (l, l_val, r, r_val)

def linear_inperpolation(x_values, y_values, x):
    """
    Выполняет линейную интерполяцию. 

    :param x_values: Список значений x (узлов интерполяции).
    :param y_values: Список значений y (значений функции в узлах интерполяции).
    :param x: Точка, в которой производится интерполяция.
    :return: Значение интерполянта в точке x.
    """
    
    if len(x_values) != len(y_values):
        raise ValueError("Длины x_values и y_values должны совпадать.")
        
    if len(x_values) == 0 or len(y_values) == 0:
        return 0

    for i,x_i in enumerate(x_values):
        if  x_i == x:
            return y_values[i]

    l, l_val, r, r_val = find_two_nearest_points(x_values, x)
        
    result = y_values[l]*(x - r_val)/(l_val - r_val) + y_values[r]*(x - l_val)/(r_val - l_val)

    return result

def parabolic_interpolation(x_values, y_values, x):
    """
    Выполняет параболическую интерполяцию.

    :param x_values: Список значений x (узлов интерполяции).
    :param y_values: Список значений y (значений функции в узлах интерполяции).
    :param x: Точка, в которой производится интерполяция.
    :return: Значение интерполянта в точке x.
    """
    
    if len(x_values) != len(y_values):
        raise ValueError("Длины x_values и y_values должны совпадать.")

    if len(x_values) == 0 or len(y_values) == 0:
        return 0

    for i,x_i in enumerate(x_values):
        if  x_i == x:
            return y_values[i]
    
    l_count = 0
    for i, x_i in enumerate(x_values):
        if x > x_i:
            l_count+=1
    
    r_count = 0
    reversed_x = x_values[::-1]
    for i, x_i in enumerate(reversed_x):
        if x< x_i:
            r_count+=1
    
    assert l_count >= 2 and r_count>=2, f"x = {x} не лежит во внутреннем отрезке между параболами. По этим данным нельзя осуществить параболическую интерполяцию"

    l_1, l_val_1, r_1, r_val_1 = find_two_nearest_points(x_values, x) #i, i+1
    l_2, l_val_2, _, _ = find_two_nearest_points(x_values, l_val_1) #i-1 
    _, _, r_2, r_val_2 = find_two_nearest_points(x_values, r_val_1) #i+2

    p1 = (x - l_val_1)*(x - r_val_1)/((l_val_2 - l_val_1)*(l_val_2 - r_val_1)) #i-1 (l_val_2)
    p2 = (x - l_val_2)*(x - r_val_1)/((l_val_1 - l_val_2)*(l_val_1 - r_val_1)) #i (l_val_1)
    p3 = (x - l_val_1)*(x - l_val_2)/((r_val_1 - l_val_1)*(r_val_1 - l_val_2)) #i+1 (r_val_1)
    p4 = (x - l_val_1)*(x - r_val_1)/((r_val_2 - l_val_1)*(r_val_2 - r_val_1)) #i+2 (r_val_2)

    l1 = p1*y_values[l_2] + p2*y_values[l_1] + p3*y_values[r_1]
    l2 = p2*y_values[l_1] + p2*y_values[r_1] + p4*y_values[r_2]

    result = (l1+l2)/2

    return result

