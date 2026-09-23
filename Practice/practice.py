
# import sqlite3
# import json


# name = "Bilal"
# age = 25
# university = "Saarland University Saarbrucken"
# cgpa = 3.16
# is_student = True
# is_Employee = False
# print(f"My name is {name}. I am {age} years old. I study at {university}. My CGPA is {cgpa}. Is student: {is_student}. Is employee: {is_Employee}. \n")

# total = age * cgpa
# print(total)

# city = "Saarbrucken"
# print(f"\n I live in {city}.")

# MODEL = "LLAMA 3.2"
# DB = "SQLITE3"

# print(f"{MODEL} + {DB}")


# def sayHello(name):
#     print(f"Hello {name}")


# sayHello("Nimra")


# def multiply(a, b):
#     return a*b


# response = multiply(4, 9)
# print(f"Multiplication result: {response}")


# def GTP(city):

#     prices = {
#         "islamabad": 100,
#         "karachi": 600
#     }
#     return prices.get(city.lower())


# print(GTP("Islamabad"))


# def calculate_square(number):
#     return number * number


# n = 5
# m = 10

# calculate_square(n)
# calculate_square(m)

# print(f"Square of {n} is: {calculate_square(n)}")
# print(f"Square of {m} is: {calculate_square(m)}")


# # Dictionaries

# student = {
#     "name": "Bilal",
#     "age": 25,
#     "university": "Air University Islamabad"
# }

# for intro, data in student.items():
#     print(intro, data)

# print(student)

# print(student["name"])

# print(student.get("age"))

# ticket_prices = {
#     "london": 799,
#     "berlin": 599,
#     "paris": 699
# }

# print(ticket_prices["london"])
# print(ticket_prices["berlin"])

# student = {
#     "name": "Bilal",
#     "age": 23
# }

# for intro, data in student.items():
#     print(intro, data)

# print(student.get("name"))
# print(student.get("age"))

# print(student.get("cgpa", "Unknown"))

# print(student.get("dubai", "Unknown"))

# print(student.get("city", "Unknown City"))

# ticket_price = {
#     "london": 8989,
#     "islamabad": 9080980,
#     "newyork": 898989
# }

# for city, price in ticket_price.items():
#     print(f"{city} and {price}")
#     print(city, price)


# student_marks = {
#     "Math": 90,
#     "English": 85,
#     "Python": 95
# }

# for subjects, marks in student_marks.items():
#     print(subjects, marks)

# name = "BILAL"

# print(name.lower())

# city = "islamabad"

# if city.lower() == "kahuta":
#     print("You selected kahuta")
# elif city.lower() == "paris":
#     print("You selected paris")
# else:
#     print("Mistake Bro")


# def get_tickets_price(city):
#     price = {
#         "london": 8989,
#         "paris": 8989
#     }
#     city = city.lower()
#     print(price.get(city, "Unknown"))


# get_tickets_price("London")
# get_tickets_price("Berlin")

# country = "PAKISTAN"

# if (country.lower() == "pakistan"):
#     print("Correct Country")

# # Json dumps loads


# student = {
#     "name": "Bilal",
#     "age":  23
# }

# json_string = json.dumps(student)
# print(json_string)
# print(type(json_string))

# json_string = '{"name": "Bilal" , "age":23}'

# print(json.loads(json_string))

# print(student)
# print(student["name"])

# arguments = '{"city" : "london" , "passengers": 2}'

# data = json.loads(arguments)

# print(data["city"])

# print(data["passengers"])

# student = {
#     "name": "Bilal",
#     "course": "Python",
#     "level": "Beginner"
# }

# studentData = json.dumps(student)

# print(studentData)

# studentDataB = json.loads(studentData)

# print(studentDataB)

# print(studentDataB["name"])

# # List

# fruits = ["apple", "banana", "mango"]
# print(fruits)

# print(fruits[0])
# print(fruits[2])

# for fruit in fruits:
#     print(fruit)

# models = [
#     "Llama",

#     "Qwen",

#     "GPT"
# ]

# print(models[0])
# print(models[-1])

# for model in models:
#     print(model)

# fruits = ["apple", "banana"]
# fruits.append("mango")
# print(fruits)

# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)

# responses = []
# responses.append("Hello")
# responses.append("AI Chatgpt ")
# print(responses)

# models = []

# models.append("Llama")
# models.append("Qwen")
# models.append("GPT")
# print(models)

# languages = []
# languages.append("Python")
# languages.extend(["German", "English"])
# MoreAdditions = ["French", "Spanish"]
# languages.extend(MoreAdditions)
# print(languages)


# temperature = 35

# if temperature > 30:
#     print("It is hot")
# else:
#     print("Its not hot")


# count = 1

# while count < 3:
#     print(count)
#     count += 1

# number = 1

# while count <= 5:
#     print(count)
#     count += 1

# languages = ["German", "English"]
# for lan in languages:
#     print(lan)

# # with open("example.txt", "w") as f:
# #     f.write("Hello Bilal")

# # with open("example.txt" , "r") as f:
# #     f.read()

# with open("example.txt", "w") as f:
#     f.write("Hello Bilal Done ")


# # with sqlite3.connect("prices.db") as connection:
# #     cursor = connection.cursor()

# #     cursor.execute(
# #         "CREATE TABLE IF NOT EXISTS prices (city TEXT, price INTEGER)")
# #     cursor.execute(
# #         "INSERT OR IGNORE INTO prices (city , price) VALUES ('london' , 999)")

# #     cursor.execute("Select * from prices")

# #     results = cursor.fetchall()

# #     for row in results:
# #         print(f"City : {row[0]}, Price: ${row[1]}")

# # with sqlite3.connect("prices.db") as connection:
# #     cursor = connection.cursor()
# #     cursor.execute(
# #         "CREATE TABLE IF NOT EXISTS prices(city TEXT , price  INTEGER)")
# #     cityName = "London , Berlin , Paris"
# #     cityPrice = 999 , 978 , 565
# #     cursor.execute(
# #         "INSERT OR IGNORE INTO prices(city , price) VALUES(? , ?) ", (cityName, cityPrice))

# #     searchCity = "london"
# #     cursor.execute("SELECT price FROM prices where city = ?", (searchCity,))

# #     result = cursor.fetchone()

# # if result:
# #     print(f"{result[0]}")
# # else:
# #     print(f"Error")

# with sqlite3.connect("school.db") as connection:
#     cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS students")

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students
#    (name TEXT,  age INTEGER , city TEXT)""")

# nameData = "Ali"
# ageData = 7989
# cityData = "Karachi"
# cursor.execute(
#     "INSERT OR IGNORE INTO students(name, age , city) VALUES(?,?,?)", (nameData, ageData, cityData))

# nameUser = "Ali"
# cityUser = "Karachi"

# cursor.execute("SELECT age  FROM students WHERE name = ? AND city = ?",
#                (nameUser, cityUser))

# result = cursor.fetchall()

# print(result)

# if result:
#     print(f"{result[0][0]}")
# else:
#     print("Error")


# age = 20

# status = "Adult" if age >= 20 else "Minnor"
# print(status)

# finish_reason = "stop"
# message = "AI finished" if finish_reason == "stop" else "AI working"
# print(message)

# age = 20
# if age >= 20:
#     statuss = "Adult"
# else:
#     statuss = "Minnor"

# print(statuss)

# # Index

# universityStudent = ("Bilal", 3.16, "SaarlandUniversity")

# print(universityStudent[0])
# print(universityStudent[1])


# Python classes and objects:
from openai import OpenAI
import requests
# from pydantic import BaseModel


# class Item(BaseModel):
#     title: str
#     price: float


# iphone = Item(title="Iphone-18", category="apple", price=65)
# print(iphone.title)


# url = "https://httpbin.org/post"

# payload = {"role": "user", "content": "Hello I am Bilal"}

# response = requests.post(url, payload)
# print(response.status_code)
# print(response.json())


# client = OpenAI(base_url="http://localhost:11434/v1", api_key="Anything")

# response = client.chat.completions.create(
#     model="llama3.2",
#     messages=[{
#         "role": "user", "content": "Hello illama what is api"
#     }]
# )

# print(response.choices[0].message.content)


class Item:
    def __init__(self, title: str, category: str, prices: int):
        self.title = title
        self.category = category
        self.prices = prices

    def __repr__(self) -> str:
        return f"<{self.title} = ${self.prices}>"


item = Item(title="Phone", category="Electronics", prices=500)

print(item)

age = 20

status = "Adult" if age >= 20 else "Mirror"
print(status)


class Dog:
    def __init__(self, name, breed) -> str:
        self.name = name
        self.breed = breed

    @classmethod
    def from_string(cls, dog_str: str):
        name, breed = dog_str.split("-")
        return cls(name, breed)

    @staticmethod
    def calculate_human_years(dog_age: int) -> int:
        return dog_age * 6


newDog = Dog.from_string("Muhammad-Bilal")
newDog = Dog.calculate_human_years(8)

#########################################
