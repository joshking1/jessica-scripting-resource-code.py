#!/usr/bin/python3

# practice a lot tomorrow 
class WarrenBuffet:
    # the class attributes 
    nationality = "American"
    birthplace = "Omaha, Nebraska"
    occupation = "An Investor, and Philanthropist"
    known_for = "Starting the company that has becaome successful in investment"
    quotes = [
        "Rule No. 1: Never lose money.",
        "Rule No. 2: Never forget rule No.1.",
        "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price.",
        "The stock market is a device for transferring money from the impatient to the patient."
    ]

    def __init__(self, name, age, net_worth, company, investment_strategy, philanthropy, education, books, investment_portfolio, Berkshire_Hathaway):
        # These are the self attributes that are related to the instances created under the class
        self.name = name
        self.age = age
        self.net_worth = net_worth
        self.company = company
        self.investment_strategy = investment_strategy
        self.philanthropy = philanthropy
        self.education = education
        self.books = books
        self.investment_portfolio = investment_portfolio
        self.Berkshire_Hathaway = Berkshire_Hathaway
# Now it is time to create the behaviors and the actions related to the objects created under the class 
# Creating an instance of the WarrenBuffet class
    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Net Worth:", self.net_worth)
        print("Company:", self.company)
        print("Investment Strategy:", self.investment_strategy)
        print("Philanthropy:", self.philanthropy)
        print("Education:", self.education)
        print("Books:", self.books)
        print("Investment Portfolio:", self.investment_portfolio)
        print("Berkshire Hathaway:", self.Berkshire_Hathaway)

# Creating an instance for the class     
buffett = WarrenBuffet(
    name="Warren Buffett",
    age=91,
    net_worth="$100 billion",
    company="Berkshire Hathaway",
    investment_strategy="Value investing",
    philanthropy="Active philanthropist",
    education="Columbia University",
    books=["The Snowball", "Buffett: The Making of an American Capitalist"],
    investment_portfolio=["Coca-Cola", "Apple", "American Express"],
    Berkshire_Hathaway=True
)

# Accessing the class attributes
print("Nationality:", WarrenBuffet.nationality)
print("Birthplace:", WarrenBuffet.birthplace)
print("Occupation:", WarrenBuffet.occupation)
print("Known For:", WarrenBuffet.known_for)
print("Quotes:", WarrenBuffet.quotes)

# Let us call a method to perfom a certain 

print(buffett.display_information())