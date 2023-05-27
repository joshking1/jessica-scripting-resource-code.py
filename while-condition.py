#!/usr/bin/python3 

# This code will be more sophisticated. 
# Do not worry, I will go through it with you in the next session. 

customer_name = ""
# In this code snippet, the while loop will continue until the input stored in customer_name consists only of alphabetic characters. 
# The isalpha() method is used to check if the input is a valid string
while not customer_name.isalpha():
    customer_name = input("What is your name? The name should contain ONLY letters and no space between first and lastname: ")
# If the customer enters a non-string input (e.g., an integer), the loop will prompt them to enter a valid string again. 
# Once a valid string is entered, the loop will exit, and the customer's name will be stored in the customer_name variable.

customer_age = ""

while not customer_age.isdigit(): # we going to check whether the statement is true
    customer_age = input("How old are you,(only digits will be accepted) {}?: ".format(customer_name))

customer_email = ""

while not customer_email.isalpha():
    
    customer_email = str(input("Please provide your email address: "))

customer_phone = ""

while not customer_phone.isalpha():
    customer_phone = int(input("What is your phone number?: "))

customer_interests = ""
while not customer_interests.isalpha():
    customer_interests = str(input("What are your primary interests or hobbies?: "))
customer_location = ""
while not customer_location.isalpha():
    customer_location = str(input("Where are you located?: "))

customer_budget = ""
while not customer_budget.isdigit():
    customer_budget = int(input("What is your budget range for the product or service you are interested in?: "))


print("Thank you for sharing your answers, {}. We appreciate your time.".format(customer_name))

print("Based on the information you provided, we would like to inform you about an exciting project we are working on. Our manager aims to enhance customer satisfaction and loyalty through various initiatives. The project focuses on improving the overall customer experience and personalizing our offerings to better meet your needs.")

print("We would love to hear your thoughts on the following questions to help us shape the project according to your preferences:")

# Add more questions specific to the project

print("Thank you for your valuable input, {}. Your feedback will be instrumental in making this project a success.".format(customer_name))
