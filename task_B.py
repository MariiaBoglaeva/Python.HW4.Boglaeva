# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# *Файлы с многочленами сформированы в конце задания А

data = open(f'equation1.txt', 'r')
for line in data:
    polynomial_1 = line
data = open(f'equation2.txt', 'r')
for line in data:
    polynomial_2 = line


def create_dict(polynomial: str):
    coeff_list = polynomial.replace("+", " ").split()
    coeff_dict = {}
    for item in coeff_list:
        if item.startswith("x"):
            item = item.replace("x", "1*x")
        elif item.startswith("-x"):
            item = item.replace("x", "-1*x")
        if not "*" in item:
            coeff_dict[0] = int(item)
        elif item.count("*") == 1:
            key = 1
            cut_value = int(item.index("*"))
            coeff_dict[key] = int(item[0:cut_value])
        else:
            cut_key = int(item.index("*"))
            key = int(item[(cut_key + 4):len(item)])
            cut_value = int(item.index("*"))
            coeff_dict[key] = int(item[0:cut_value])
    return coeff_dict


polynomial_1_dict = create_dict(polynomial_1)
print(polynomial_1_dict)
polynomial_2_dict = create_dict(polynomial_2)
print(polynomial_2_dict)


def sum_dict(dict_1: dict, dict_2: dict):
    count = len(dict_1)
    if count < len(dict_2):
        count = len(dict_2)
    dict_sum = {}
    for c in dict_1.keys():
        dict_sum[c] = dict_1.get(c, 0) + dict_2.get(c, 0)
    for k in range(count):
        if dict_sum.get(k) == None:
            dict_sum[k] = dict_1.get(k, 0) + dict_2.get(k, 0)
    return dict_sum


polynomial_3_dict = sum_dict(polynomial_1_dict, polynomial_2_dict)


def create_equation(coeff_dict: dict):
    equation = ""
    for i in range(len(coeff_dict), -1, -1):
        if i > 1:
            if coeff_dict.get(i, 0) == 0:
                equation += f""
            elif coeff_dict.get(i) == 1:
                equation += f"+ x**{i} "
            elif coeff_dict.get(i) < 0:
                equation += f"{coeff_dict[i]}*x**{i} "
            else:
                equation += f"+ {coeff_dict[i]}*x**{i} "
        elif i == 1:
            if coeff_dict.get(i, 0) == 0:
                equation += f""
            elif coeff_dict.get(i) == 1:
                equation += f"+ x "
            elif coeff_dict.get(i) < 0:
                equation += f"{coeff_dict[i]}*x"
            else:
                equation += f"+ {coeff_dict[i]}*x"
        else:
            if coeff_dict.get(i, 0) == 0:
                equation += f""
            elif coeff_dict.get(i) < 0:
                equation += f"{coeff_dict[i]}"
            else:
                equation += f"+ {coeff_dict[i]}"
    if coeff_dict.get(len(coeff_dict) - 1) > 0:
        return equation[2:]
    else:
        return equation


print(polynomial_3_dict)
polynomial_summ = create_equation(polynomial_3_dict)
print(f"{polynomial_summ} = 0")
