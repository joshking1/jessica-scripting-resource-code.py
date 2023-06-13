def print_personal_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    country_of_origin = input("Enter your country of origin: ")
    favorite_country = input("Enter your favorite country: ")
    president = input("Enter the president of your country: ")
    favorite_food = input("Enter your favorite food: ")
    favorite_destination = input("Enter your favorite tourist destination: ")
    
    print("My name is {} {}. I am from {}. My favorite country is {}. The president of my country is {}. My favorite food is {}. My favorite tourist destination is {}.".format(first_name, last_name, country_of_origin, favorite_country, president, favorite_food, favorite_destination))

# Example usage:
print_personal_info()
