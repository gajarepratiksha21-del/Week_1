# Name:Gajare Pratiksha Navnath
# Project: Personal Information Program
print("====Welcome to Personal Information Program ====")

"""Static Information"""
name="Pratiksha"   # Stored name to variable(i.e name) used string data type
print("Name:",name)  # Displayed name using print function
age=20             # Stored age to variable age  used integer data type
print("Age:",age)    # Displayed age using print function
city="Pune"        # Stored Pune to variable city used string data type
print("City:",city)   # Displayed city using print function
hobby="Reading"    #Stored Reading to variable hobby used string data type
print("Hobby:",hobby) # Displayed hobby using print function


#  Get user input
favorite_food = input("Enter your favorite food: ")

if favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food?: ")


favorite_color = input("Enter your favorite color: ")

if favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? :")

# Calculate age in months
age_months = age * 12

# Welcome message
print("\n===== Welcome =====")

# Display information
print("\n===== Personal Information =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print("\n===== Favorites =====")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

print("\n===== Additional Information =====")
print(f"Age in Months: {age_months}")

print("\n===== Goodbye =====")
print(f"Thank you, {name}! Have a nice day!")


