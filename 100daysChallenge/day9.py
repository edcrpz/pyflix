# Dictionaries

# dictionary = {"Key": "Value", "Key2": "Value", etc.}
# Key can be number, variable, or string

# programming_dictionary = {
#     "Bug": "An error in a program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# Retrieve an value of key in dictionary
# print(programming_dictionary["Bug"])

# Retrieve a key:
# print(programming_dictionary[0]) or for item in dictionary

# Calling an item:

# How to print Steak value?

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# Answer:  print(order["main"][2][0])
# checks the main key for order, selects "2" key, and index 0 of list- Steak

# Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating empty dictionary
# empty_dictionary = {}

# Wipe out dictionary
# programming_dictionary = {}

# Edit an item
# programming_dictionary["Bug"] = "This is the new value for Bug."

# Loop through a dictionary
# for item in programming_dictionary:
#     print(item)
#  it only returns Keys only

# ======================================================================

# print("Exercise 9.1 - Grading program")
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
# for student in student_scores:  # for every key (student)
#     if 100 >= student_scores[student] > 90:   # checks value of student (for Harry, it's 81)
#         student_grades[student] = "Outstanding"  # add item student_grades["Harry"] = "Outstanding
#     elif 90 >= student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif 80 >= student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)

# ======================================================================

# Nested Dictionaries
# {
#     Key: [List],
#     Key2: {Dict},
# }

# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],  # list of cities traveled in france
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# Nesting a Dictionary in a Dictionary (description for each item in value)
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},  # list of cities traveled in france
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }

# Multiple dictionaries in a Single list

# my_travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
#         "total_visits": 12
#     }
# ]

# ======================================================================

print("Exercise 9.2 - Dictionary in List")

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(countries, no_of_visits, cities_visited):

    new_country = {}
    new_country["country"] = countries
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_visited

    travel_log.append(new_country)
    # travel_log was a list, so need to append

    print(f"You have visited {countries} {no_of_visits} times.")
    print(f"You've been to {cities_visited[0]} and {cities_visited[1]}")


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)

# ======================================================================

