# Normalize data
# Trim names, separate scores by column and convert into integer, delete duplicate names and keep first occurence
# Score range = 0-100
# Raise Custom Error when trying to add another score to a student
# vectorize every student score with np.mean
# .lock method on student, .add_score method, .average method (np.mean)
# 2 Custom Exceptions: InvalidScoreError, and StudentRecordLockedError
# clean raw_rows, buil;d student objects
# return failures like parsing or validation failures.
# Then a ranking function that uses sorted() with lambda key
# to sort students by average score in descending order



#Running your script should print, in order:

#1. Each successfully built student via print(student).
#2. The full list of built students in one call, e.g. print(students).
#3. One line per failed row (not including dropped duplicates): Skipped row: {original raw dict} -> reason: {error}.
#4. One manual demonstration: build a valid Student, lock it, attempt .add_score(), catch your custom exception, print it.
#5. The ranked list, averages shown to 2 decimal places: 1. Amara — 85.00 avg.



import pandas as pd
import numpy as np

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def add_score(score):
        #append scores









raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

df = pd.DataFrame(raw_rows)
df.drop_duplicates()
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["name"] = df["name"].str.strip().lower().replace("_", " ")


print(df)