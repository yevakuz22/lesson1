# import inspect
# import sys
#
# import requests
#
# class Human:
#      pass
#
#
# def my_function():
#      pass
#
#
# print(type(requests))
# number = 10
# print(type(number))
#
# help(requests.__cake__)
# print(Human.__name__)
# print(my_function.__name__)
#
# print(dir(Human))
#
#
# number_list = [1, 2, 3]
# print(dir(number_list))
# print(hasattr(number_list, "pop"))
# print(getattr(number_list, "max"))
#
#
# print(callable(my_function))
#
# class First_Class:
#     pass
#
#
# class Second_Class(First_Class):
#     pass
#
#
# print(issubclass(First_Class, Second_Class))
# print(issubclass(Second_Class, First_Class))
#
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isfunction(my_function()))
# print(inspect.getmodul(requests.get()))
# print(inspect.getmodul(list()))
#
#
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.argv)
#
# # for module_name, module_path in sys.modules.items():
# #     print(module_name, module_path)
#
# for _ in dir(__builtins__):
#     print()



# try:
#     print(123)
#     print("Hello im in try")
#     print(10 / 0)
# except NameError:
#     print("Помилка написання назви")
# except ZeroDivisionError as error:
#     print(error)
#
#
# try:
#     print(10)
# except:
#     print("Якась помилка")
# finally:
#     print("немає помилок, все виконано успішно")
#
#
# print("hello im out try :)")
# print(10 / 0)



# def checker(var):
#     if (var < 10):
#         raise TypeError("Число має бути більшим або дорівнювати 10")
#     else:
#         return var
#
# numbers = 3
# print(checker(number))



# class BuildingError(Exception):
#
#     def __str__(self):
#         return f"Введені не вірні данні"
#
#     def checker(material_count, limit):
#         if material_count < limit:
#             raise BuildingError("матеріалів не достатньо")
#         else:
#             print("матеріалів не достатньо")
#
# material = 120
# checker(material, 450)
#
#
#
# class some_function(self):
#     print("Я щось тут роблю (напевно)")
#
#
#
# class Second_Class(First_Class):
#     pass
#
# some_object = Second_Class()
# some_object.some_function()





try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if num2 == 0:
        print("Ділення на нуль неможливе.")
    else:
        result = num1 / num2
        print("Результат ділення:", result)

except ValueError:
    print("Введено некоректні дані, будь ласка, введіть числа.")
except Exception:
    print("Виникла помилка:")




























