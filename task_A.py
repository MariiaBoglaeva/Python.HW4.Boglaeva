# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# А:
import random


def create_coefficient(num: int):
    coeff_dict = {}
    for k in range(num, -1, -1):
        coeff_dict[k] = random.randint(-100, 101)
    if coeff_dict[num] == 0: #множитель у наибольшей степени не должен быть равен 0. Иначе это будет многочлен другой степени уже
        coeff_dict[num] = random.randint(1, 101)
    return coeff_dict


def create_equation(coeff_dict: dict):
    equation = ""
    for i in range(len(coeff_dict)-1, -1, -1):
        if i > 1:
            if coeff_dict[i] == 0:
                equation += f""
            elif coeff_dict[i] == 1:
                equation += f"+ x**{i} "
            elif coeff_dict[i] < 0:
                equation += f"{coeff_dict[i]}*x**{i} "
            else:
                equation += f"+ {coeff_dict[i]}*x**{i} "
        elif i == 1:
            if coeff_dict[i] == 0:
                equation += f""
            elif coeff_dict[i] == 1:
                equation += f"+ x "
            elif coeff_dict[i] < 0:
                equation += f"{coeff_dict[i]}*x"
            else:
                equation += f"+ {coeff_dict[i]}*x"
        else:
            if coeff_dict[i] == 0:
                equation += f""
            elif coeff_dict[i] < 0:
                equation += f"{coeff_dict[i]}"

            else:
                equation += f"+ {coeff_dict[i]}"
    if coeff_dict[len(coeff_dict)-1] > 0:
        return equation[1:]
    else:
        return equation


n = int(input("Введите максимальную степени: "))
n_coeff = create_coefficient(n)
print(n_coeff)
print(f"{create_equation(n_coeff)} =0")

#B:
# Создаем файлы с многочленами:
for i in range(2):
    data = open(f"equation{i + 1}.txt", 'w')
    n_coeff = create_coefficient(n)
    data.writelines(create_equation(n_coeff))

