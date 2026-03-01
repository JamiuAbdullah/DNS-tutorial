name = "Jamiu Abdullah Baba"
age = 18
print(f" Hello, my name is {name} and I am {age} years old." )


from datetime import datetime 
name = input(" Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
age = current_year - birth_year

print(f"Hello {name}, you are {age} years old")