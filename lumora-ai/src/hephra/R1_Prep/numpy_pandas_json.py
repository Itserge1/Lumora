# Pandas & NumPy JSON Data Exercises
# Practice creating, storing, and loading JSON data with DataFrames

import csv
import json
import numpy as np
import pandas as pd
from pathlib import Path

# ================================
#        HELPER FUNCTIONS
# ================================
# Save Data into a JSON file
def save_to_json_file(file_name, data):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving data to {file_name}: {e}")
        raise

# Get file path
def get_file_path(file_name):
    file_path = Path(__file__).parent / f"{file_name}"
    return file_path


# ============================================================
# EXERCISE 1: Create a DataFrame and save it as JSON
# ============================================================
print("EXERCISE 1: Create and Save DataFrame as JSON")
print("-" * 50)

# TODO: Create a DataFrame with the following data:
# - Names: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# - Ages: [25, 30, 35, 28, 32]
# - Scores: [85.5, 92.3, 78.9, 88.7, 95.1]

# Your code here:
data1 = {
        "Names": ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        "Ages": [25, 30, 35, 28, 32],
        "Scores": [85.5, 92.3, 78.9, 88.7, 95.1]
    }

data2 = {
    "Age": pd.Series([25, 30]),
    "Score": pd.Series([85, 90, 95])
}

data3 = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30},
    {"Name": "Jhon"}
]

data4 = [
    ["Alice", 25],
    ["Bob", 30]
]

data5 = np.array([[1, 2], [3, 4]])

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(
    data4,
    columns=["Name", "Age"]
)
df5 = pd.DataFrame(
    data5,
    columns=["A", "B"]
)

# print(df1)
# print("\n")
# print(df2)
# print("\n")
# print(df3)
# print("\n")
# print(df4)
# print("\n")
# print(df5)


# TODO: Save this DataFrame to a JSON file called 'data.json'
# Hint: Use df.to_json()

# Your code here:
# json_str = df1.to_json()
# json_data = json.loads(json_str)
# json_data = df1.to_dict()
# json_data = df1.to_dict(orient="columns")
# json_data = df1.to_dict(orient="records")
# save_to_json_file("data.json", json_data)


# # ============================================================
# # EXERCISE 2: Load JSON data into a DataFrame
# # ============================================================
# print("\nEXERCISE 2: Load JSON into DataFrame")
# print("-" * 50)
#
# # TODO: Load the JSON file you created above back into a new DataFrame
# # Hint: Use pd.read_json()
#
# # Your code here:
# file_path = get_file_path("data.json")
# file_path_1 = get_file_path("data1.json")
#
# df_loaded = pd.read_json(file_path)
# with open(file_path_1, "r") as f:
#     data = json.load(f)
#     df_loaded_1 = pd.DataFrame(data["all_users"])
#
# print(df_loaded)
# print(df_loaded_1)
#
#
# # ============================================================
# # EXERCISE 3: Create nested JSON data
# # ============================================================
# print("\nEXERCISE 3: Work with Nested JSON")
# print("-" * 50)
#
# # TODO: Create this nested structure as a dictionary:
# # [{
# #     'id': 1,
# #     'name': 'John',
# #     'grades': {'math': 90, 'science': 85, 'english': 88}
# # },
# # {
# #     'id': 2,
# #     'name': 'Sarah',
# #     'grades': {'math': 95, 'science': 92, 'english': 90}
# # }]
#
# # Your code here:
# data = [
#     {
#         'id': 1,
#         'name': 'John',
#         'grades': {'math': 90, 'science': 85, 'english': 88}
#     },
#     {
#         'id': 2,
#         'name': 'Sarah',
#         'grades': {'math': 95, 'science': 92, 'english': 90}
#     }
# ]
#
# # TODO: Convert to DataFrame and flatten the 'grades' column
# # Hint: Use pd.json_normalize()
#
# # Your code here:
# df = pd.DataFrame(data)
# print(df)
#
# df_3 = pd.json_normalize(df["grades"])
# print(df_3)
#
# df = df.drop(columns=["grades"],axis=1)
# print(df)
#
# df = pd.concat([df, df_3], axis=1)
# print(df)

#
# # ============================================================
# # EXERCISE 4: Use NumPy to generate data, then save as JSON
# # ============================================================
# print("\nEXERCISE 4: NumPy + DataFrame + JSON")
# print("-" * 50)
#
# # TODO: Create a DataFrame using NumPy arrays:
# # - Generate 10 random integers between 1-100 for 'values'
# # - Generate 10 random floats between 0-1 for 'probabilities'
# # - Create an array of consecutive dates starting from '2024-01-01' (10 days)
#
# # Hints:
# # np.random.randint(1, 100, size=10)
# # np.random.random(size=10)
# # pd.date_range('2024-01-01', periods=10)
#
# # Your code here:
# rng = np.random.default_rng()
# all_ints = rng.integers(1, 101, size=10)
# all_floats = rng.uniform(0, 1, size=10)
# start_date = np.datetime64('2024-01-01')
# all_dates = start_date + np.arange(10)
#
# df_4 = pd.DataFrame({
#     'date': all_dates,
#     'values': all_ints,
#     'probabilities': all_floats
# })
#
# # TODO: Save this DataFrame as JSON with date formatting
# # Hint: Use date_format='iso' parameter
#
# # Your code here:
# # df4.to_json('data4.json', date_format='iso')
#
# df_4_data_str = df_4.to_json(orient="records", date_format="iso")
# df_4_data = json.loads(df_4_data_str)
# file_path = get_file_path("df_4_data.json")
# save_to_json_file(file_path, df_4_data)
#

#
# # # ============================================================
# # # EXERCISE 5: Complex JSON manipulation
# # # ============================================================
# # print("\nEXERCISE 5: Advanced JSON Operations")
# # print("-" * 50)
# #
# # # TODO: Create a JSON string (not a file) with this data:
# json_string = '''
# {
#     "students": [
#         {"name": "Alex", "age": 20, "courses": ["Math", "Physics"]},
#         {"name": "Beth", "age": 22, "courses": ["Chemistry", "Biology"]},
#         {"name": "Carl", "age": 21, "courses": ["Math", "Chemistry", "Physics"]}
#     ]
# }
# '''
#
# # TODO:
# # 1. Parse this JSON string into a Python dictionary
# # 2. Extract the 'students' list
# # 3. Create a DataFrame from it
# # 4. Add a new column 'num_courses' that counts the courses for each student
# # 5. Save the result as 'students.json'
#
# # Your code here:
# # data_dict = json.loads(json_string)
# # students = data_dict['students']
# # df5 = pd.DataFrame(students)
# # df5['num_courses'] = ...
#
#
#
# data_dict = json.loads(json_string)
# df_5 = pd.DataFrame(data_dict["students"])
# print(df_5)
# df_5["num_courses"] = df_5["courses"].apply(len)
# df_5["is_adult"] = df_5["age"].apply(lambda x: 1 if x > 18 else 0)
# print(df_5)

#
# # ============================================================
# # BONUS CHALLENGE
# # ============================================================
# print("\nBONUS: Create a CSV, convert to JSON, then back to DataFrame")
# print("-" * 50)
#
# # TODO:
# # 1. Create a DataFrame with at least 3 columns and 5 rows
# # 2. Save it as CSV
# # 3. Load the CSV back
# # 4. Convert to JSON format
# # 5. Load the JSON back into a new DataFrame
# # 6. Compare the original and final DataFrames
#
# # Your code here:
# data = [
#     {
#         "name": "Alice",
#         "age": 25,
#         "email": "alice@gmail.com",
#         "subscription": 0
#     },
#     {
#         "name": "Mark",
#         "age": 17,
#         "email": "mark@gmail.com",
#         "subscription": 1
#     },
#     {
#         "name": "Jonny",
#         "age": 30,
#         "email": "jonny@gmail.com",
#         "subscription": 1
#     },
#     {
#         "name": "Lara",
#         "age": 20,
#         "email": "lara@gmail.com",
#         "subscription": 1
#     },
#     {
#         "name": "Fatima",
#         "age": 30,
#         "email": "fatima@gmail.com",
#         "subscription": 0
#     }
# ]
#
# df_6 = pd.DataFrame(data)
# df_6.to_csv("costumers.csv", index=False)
# print(df_6)
#
# with open("costumers.csv", "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     csv_data = list(reader)
#
# new_df_6 = pd.DataFrame(csv_data)
# print(new_df_6)
#
# print(df_6["age"].astype(int))
#
#
# new_df_6["age"] = new_df_6["age"].astype(df_6["age"].dtype)
# new_df_6["subscription"] = new_df_6["subscription"].astype(df_6["subscription"].dtype)
#
# print(df_6.dtypes)
# print(new_df_6.dtypes)
#
# print(df_6.equals(new_df_6))
#
#
# print("\n" + "="*50)
# print("Complete the exercises above!")
# print("Check your work by printing the DataFrames and inspecting the JSON files")
# print("="*50)