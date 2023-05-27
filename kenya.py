#!/usr/bin/python3

# Let us start by creating a class called EastAfricaCountries

class EastAfricaCountries:
    # Let us add attributes associated with EastAfricaCountries class 
    # Attributes are nothing but just variables used to store specific information related to class.
    country1 = "Kenya"
    country2 = "Tanzania"
    country3 = "Uganda"
    country4 = "Rwanda"
    country5 = "Burundi"
    country6 = "Ethiopia"
    country7 = "South Sudan"
    country8 = "Somalia"
    country9 = "Djibouti"
    country10 = "Eritrea"
    # Let us now create actions assocaited with the objects under the class 
    def __init__(self, country1, country2, country3, country4, country5,
                 country6, country7, country8, country9, country10):
        self.country1 = country1
        self.country2 = country2
        self.country3 = country3
        self.country4 = country4
        self.country5 = country5
        self.country6 = country6
        self.country7 = country7
        self.country8 = country8
        self.country9 = country9
        self.country10 = country10

    def get_country_list(self):
        return [self.country1, self.country2, self.country3, self.country4,
                self.country5, self.country6, self.country7, self.country8,
                self.country9, self.country10]

    def print_countries(self):
        for country in self.get_country_list():
            print(country)

# Let us access one of the attribute or variable under the EastAfricaCountries
print(EastAfricaCountries.country1)

# Let us create objects 

east_africa = EastAfricaCountries("Kenya", "Tanzania", "Uganda", "Rwanda", "Burundi",
                                 "Ethiopia", "South Sudan", "Somalia", "Djibouti", "Eritrea")
    
# Let us perfom some actions on the object

print(east_africa.print_countries())

