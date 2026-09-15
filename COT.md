For the first steps of creating the desired program these were the order of operations that i thought of:


1. Clean the data first into a new dataframe, using df.drop_duplicates, str.strip(), str.lower(), and str.replace().

2. Then create the student calss, every student created should have their own name and scores: self.name, etc. Every student created should be appended to the dataframe. This way we can fullfill the 1st and 2nd objectives. print the first objective by printing the students directly.

3. One line per failed row: To do this I have to do a try catch for each row when cleaning the dataframe, when cleaning fails it should print("\n").

df["students"] = df.apply(lambda row: f"{row['name']}: {row['scores]}", SORT HERE)


# Student Class
This class has a __init__, lock, and average method
Init will just be to initialize the self
Lock will be an exception to handle the range of the score being 0-100. 
The average method will compute only that students average score using np.mean to fulfill the requirements. This is not the same as computing the average of all the students scores in the cleaned dataframe. 


Testing in every way, each new student can be created like this: 

jack = Student("Mikkel", 90, 29, 100)

If im correct, in order to take in multiple scores I'll need to utilize args and kwargs. 

Data cleaning should be in one function, that way we can keep the original raw_rows, create a new cleaned dataframe of raw_rows, and another new dataframe with the new students created and cleaned as well.
