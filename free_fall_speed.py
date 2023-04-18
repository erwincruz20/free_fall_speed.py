import math

height = float(input("Введите высоту падения объекта: "))

speed = math.sqrt(2 * 9.81 * height)

print("Скорость свободного падения на высоте", height, "метров равна", speed, "метров в секунду.")
