# Personal Information Manager

## 📌 Project Description

This is my first Python project! It is a simple program that stores and displays personal information. The program also takes the user's favorite food and favorite color as input and validates empty inputs.

## 🎯 Project Objectives

- Store personal information using Python variables.
- Take user input using the `input()` function.
- Validate empty user input.
- Display information in a readable format.
- Use f-strings for formatted output.
- Calculate age in months.
- Practice basic Python programming concepts.

## 💻 Technologies Used

- Python 3

## 📋 Personal Information

===================================
       PERSONAL INFORMATION
===================================

Name: Pratiksha
Age: 20 (240 months old)
City: Pune
Hobby: Learning Music

===================================
       FAVORITE INFORMATION
===================================

Favorite Food: User Input
Favorite Color: User Input

Thank you for using the program!

## ✨ Features

- Stores name, age, city, and hobby.
- Takes favorite food from the user.
- Takes favorite color from the user.
- Checks for empty input.
- Displays information using f-strings.
- Calculates age in months.
- Provides a welcome and goodbye message.
- Uses separators to make the output readable.

## 🧪 Testing

The program was tested with different inputs.

### Test Case 1: Normal Input

Favorite Food: Pizza
Favorite Color: Blue

Expected Result:
The program displays the entered food and color correctly.

### Test Case 2: Empty Input

Favorite Food: 
Favorite Color:

Expected Result:
The program displays a message asking the user to enter valid information.

### Test Case 3: Long Input

Favorite Food: A very long food name
Favorite Color: A very long color name

Expected Result:
The program accepts the input and displays it correctly.

## 🧩 Challenges & Solutions

### Challenge 1: User might enter empty input

**Solution:**  
Added basic validation using an `if` statement to check whether the input is empty.

### Challenge 2: Formatting the output nicely

**Solution:**  
Used f-strings and separators to display the information in a clean and readable format.

### Challenge 3: Calculating age in months

**Solution:**  
Multiplied the user's age by 12 to calculate the age in months.

## 📂 Project Structure

```text
week1-personal-info/
├── personal_info.py
├── README.md
├── test_inputs.txt
└── .gitignore
