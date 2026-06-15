# Day 2 - Grade Calculator

Today, I practiced Python operators and conditional statements by building a simple Grade Calculator.

## About the Project

This program takes a student's mark as input and displays the corresponding grade based on predefined criteria.

### Grade Criteria

90 and above → Grade A
75 to 89 → Grade B
50 to 74 → Grade C
Below 50 → Grade F

## Python Code


mark = int(input("Enter a student mark:"))

if(mark >= 90):
    print("Grade A")
elif(mark >= 75 and mark <= 89):
    print("Grade B")
elif(mark >= 50 and mark <= 74):
    print("Grade C")
elif(mark <= 50):
    print("Grade F")


## Sample Output


Enter a student mark: 85
Grade B


## What I Learned

Taking input from the user.
Using comparison and logical operators.
Working with if-elif statements
Building a simple decision-making program in Python.

This project is part of my Python learning journey and daily coding practice.

Author:Yogithaa
