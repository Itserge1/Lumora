# Pandas & NumPy JSON Data Exercises
# Practice creating, storing, and loading JSON data with DataFrames

import pandas as pd
import numpy as np
import json

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
# df1 = pd.DataFrame({...})

# TODO: Save this DataFrame to a JSON file called 'data1.json'
# Hint: Use df.to_json()

# Your code here:


# ============================================================
# EXERCISE 2: Load JSON data into a DataFrame
# ============================================================
print("\nEXERCISE 2: Load JSON into DataFrame")
print("-" * 50)

# TODO: Load the JSON file you created above back into a new DataFrame
# Hint: Use pd.read_json()

# Your code here:
# df1_loaded = pd.read_json(...)
# print(df1_loaded)


# ============================================================
# EXERCISE 3: Create nested JSON data
# ============================================================
print("\nEXERCISE 3: Work with Nested JSON")
print("-" * 50)

# TODO: Create this nested structure as a dictionary:
# [{
#     'id': 1,
#     'name': 'John',
#     'grades': {'math': 90, 'science': 85, 'english': 88}
# },
# {
#     'id': 2,
#     'name': 'Sarah',
#     'grades': {'math': 95, 'science': 92, 'english': 90}
# }]

# Your code here:
# data = [...]

# TODO: Convert to DataFrame and flatten the 'grades' column
# Hint: Use pd.json_normalize()

# Your code here:
# df3 = pd.json_normalize(data)
# print(df3)


# ============================================================
# EXERCISE 4: Use NumPy to generate data, then save as JSON
# ============================================================
print("\nEXERCISE 4: NumPy + DataFrame + JSON")
print("-" * 50)

# TODO: Create a DataFrame using NumPy arrays:
# - Generate 10 random integers between 1-100 for 'values'
# - Generate 10 random floats between 0-1 for 'probabilities'
# - Create an array of dates starting from '2024-01-01' (10 days)

# Hints:
# np.random.randint(1, 100, size=10)
# np.random.random(size=10)
# pd.date_range('2024-01-01', periods=10)

# Your code here:
# df4 = pd.DataFrame({
#     'date': ...,
#     'values': ...,
#     'probabilities': ...
# })

# TODO: Save this DataFrame as JSON with date formatting
# Hint: Use date_format='iso' parameter

# Your code here:
# df4.to_json('data4.json', date_format='iso')


# ============================================================
# EXERCISE 5: Complex JSON manipulation
# ============================================================
print("\nEXERCISE 5: Advanced JSON Operations")
print("-" * 50)

# TODO: Create a JSON string (not a file) with this data:
json_string = '''
{
    "students": [
        {"name": "Alex", "age": 20, "courses": ["Math", "Physics"]},
        {"name": "Beth", "age": 22, "courses": ["Chemistry", "Biology"]},
        {"name": "Carl", "age": 21, "courses": ["Math", "Chemistry", "Physics"]}
    ]
}
'''

# TODO:
# 1. Parse this JSON string into a Python dictionary
# 2. Extract the 'students' list
# 3. Create a DataFrame from it
# 4. Add a new column 'num_courses' that counts the courses for each student
# 5. Save the result as 'students.json'

# Your code here:
# data_dict = json.loads(json_string)
# students = data_dict['students']
# df5 = pd.DataFrame(students)
# df5['num_courses'] = ...


# ============================================================
# BONUS CHALLENGE
# ============================================================
print("\nBONUS: Create a CSV, convert to JSON, then back to DataFrame")
print("-" * 50)

# TODO:
# 1. Create a DataFrame with at least 3 columns and 5 rows
# 2. Save it as CSV
# 3. Load the CSV back
# 4. Convert to JSON format
# 5. Load the JSON back into a new DataFrame
# 6. Compare the original and final DataFrames

# Your code here:


print("\n" + "="*50)
print("Complete the exercises above!")
print("Check your work by printing the DataFrames and inspecting the JSON files")
print("="*50)