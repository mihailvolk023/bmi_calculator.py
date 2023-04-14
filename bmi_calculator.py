# bmi_calculator.py

height = float(input("Введите ваш рост в метрах: "))
weight = float(input("Введите ваш вес в килограммах: "))

bmi = weight / (height ** 2)

print("Ваш индекс массы тела (BMI) составляет: ", round(bmi, 2))
