#!/usr/bin/python3

customer_name = str(input("What is your name?: "))
customer_age = int(input("How old are you, {}?: ".format(customer_name)))
customer_email = str(input("Please provide your email address: "))
customer_phone = int(input("What is your phone number?: "))

print("Thank you for providing the information, {}. We have a few more questions for you.".format(customer_name))

customer_interests = str(input("What are your primary interests or hobbies?: "))
customer_location = str(input("Where are you located?: "))
customer_budget = int(input("What is your budget range for the product or service you are interested in?: "))

print("Thank you for sharing your answers, {}. We appreciate your time.".format(customer_name))

print("Based on the information you provided, we would like to inform you about an exciting project we are working on. Our manager aims to enhance customer satisfaction and loyalty through various initiatives. The project focuses on improving the overall customer experience and personalizing our offerings to better meet your needs.")

print("We would love to hear your thoughts on the following questions to help us shape the project according to your preferences:")

# Add more questions specific to the project

print("Thank you for your valuable input, {}. Your feedback will be instrumental in making this project a success.".format(customer_name))
