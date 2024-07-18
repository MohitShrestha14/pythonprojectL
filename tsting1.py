# def gender_detail(gender_):
#     conditions = {
#         'male': 'you\'re male',
#         'female': 'you\'re female'
#     }
#     if gender_ == "male1":
#         print(f"Hello  from if condition, {conditions.get(gender_, 'MOHIT')}")
#     else:
#         print(f"Hello from else condition, {conditions[gender_]}")
#
#
# if __name__ == "__main__":
#     gender_ = input("Enter your gender: ")
#     gender_detail(gender_)
# a = [12, 4123, 324, 1, 35, 6, 7, 24, 13]
# lst = [i ^ 2 if i % 2 == 0 else i ^ 3 for i in a]
# print(lst)

# company_name = "vertex Special Technology"[::-1]
# print(company_name)

# import copy
# original = [[1, 2, 3], [4, 5, 6]]
# shallow_copy = copy.copy(original)
# print(shallow_copy)
# print(original)
#
# original_list = [[1, 2, 3], [4, 5, 6]]
# shallow_copy_list = original_list.copy()
# print(shallow_copy_list)
# print(original_list)
#
# original_dict = {'a': 1, 'b': 2}
# shallow_copy_dict = original_dict.copy()
# print(shallow_copy_dict)
# print(original_dict)

#old way (decorator)
# def make_pretty(func):
#     def inner():
#         print("I got decorated...")
#         func()
#     return inner
#
# def ordinary():
#     print("I am ordinary")
#
# decorated_func = make_pretty(ordinary)
#
# decorated_func()

#new way decorator using @

# def make_pretty(func):
#     def inner():
#         print("I got decorated...")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
# ordinary()

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
#
# divide(2,0)

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
# printer("Hello")

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         super().__init__(name, id)
#         self.lang = lang

# rohan = Employee("Rohan Das", "420")
# mohit = Programmer("Mohit", "2345", "Python")
#
# print(mohit.name)
# print(mohit.id)
# print(mohit.lang)

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.x * self.y
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius, radius)
#     def area(self):
#         return 3.14 * super().area()
#
# c = Circle(5)
# print(c.area())

# from PyPDF2 import PdfWriter
# import os
#
# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]
#
# for pdf in files:
#     merger.append(pdf)
# # for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
# #     merger.append(pdf)
#
# merger.write("merged-pdf.pdf")
# merger.close()

# char = int(input("Enter a character: ")[0])
# print(f"You entered the character: {char}")

# while True:
#     user_input = input("Enter a single-digit number (0-9): ")
#     if user_input.isdigit() and 0 <= int(user_input) <= 9 and len(user_input) == 1:
#         single_digit = int(user_input)
#         break
#     else:
#         print("Invalid input. Please enter a single-digit number.")

# print(f"You entered the single-digit number: {single_digit}")

# while True:
#     user_input = input("Enter a single-digit number (0-9): ")
#     if user_input.isdigit() and 0 <= int(user_input) <= 9 and len(user_input) == 1:
#         single_digit = int(user_input)
#         ascii_value = ord(user_input)
#         break
#     else:
#         print("Invalid input. Please enter a single-digit number.")

# print(f"You entered the single-digit number: {single_digit}")
# print(f"The ASCII value of the number {single_digit} is: {ascii_value}")

# from typing import List, Dict, Tuple, Union

# def process_numbers(numbers: List[int]) -> List[int]:
#     return [n * 2 for n in numbers]

# def get_user_info() -> Dict[str, Union[str, int]]:
#     return {"name": "Alice", "age": 30}

# def split_name(name: str) -> Tuple[str, str]:
#     return tuple(name.split())

# processed_numbers = process_numbers([1, 2, 3, 4])
# user_info = get_user_info()
# split_names = split_name("Alice 3 nepal")

# print(f"Processed Numbers: {processed_numbers}")
# print(f"User Info: {user_info}")
# print(f"Split Names: {split_names}")


# def process_items(items: list[str]):    #here [str] is type parameter
#     for item in items:
#         print(item.)

# def process_items(items_t: tuple[int, int, str], item_s: set[bytes]):
#     return items_t, items_s

# def process_items(prices: dict[str, float]):
#     for item_name, item_price in prices.items():
#         print(item_name)
#         print(item_price)
#
#
# # In python 3.10+, we can put possible types separated by a vertical bar |
# previous, Union[int, str]
# now, int | str











































