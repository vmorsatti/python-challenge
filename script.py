# Verna's Exercise on how to use defaultdict, sorted, append, items, print, join 
# for a tuple, sorted &  printing the results without formatting
#  
# NOT A CLASS EXERCISE !

# Goal is to print each state with cities listed after - one state followed by list of cities.
# Sort by state
# ADD user friendly dialog
# Run code in terminal!  It works!

 
#Here's what is supplied:
# Unsorted list of some 
# states and cities in them as tuples
state_city_list = [('TX','Georgetown'), ('CO','Denver'),('CO','Denver'), ('TX','Houston'), ('NY','Albany'), ('AK','Valdez'),('AK','Homer'),('AK','Fairbanks'),('NY', 'Syracuse'), ('NY', 'Buffalo'), 
    ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta'),('MN','St. PAUL'),('CO','Greeley'),('CO','Pueblo')]

# Take a look at it in terminal:
print() # Blank line
print("state_city_list = ")
print(state_city_list)
print()

# Get some cool tools:
import csv
from collections import defaultdict

sorted_city_list = sorted(state_city_list)
print("sorted_city_list")
print(sorted_city_list) 
    # sort the states first here
print()

# Let's tool it into a list of states with their grouped associated cities:
    # Defines cities_by_state as a defaultdict function list variable 
    # for the following tools to work on:

cities_by_state = defaultdict(list)
for state, city in sorted_city_list:
    cities_by_state[state].append(city) # tool to create a tuple of 
    # each state associated with a list of unique cities (I HAD DENVER LISTED TWICE
    # but only shows up in resutlts, once)

# Take a look at it in terminal:
print() # Blank line
print("The new list, cities_by_state is this as a result of defaultdict(list):")
print(cities_by_state) 
    #  Will print like this:  
    # {'TX': ['Austin', 'Houston', 'Dallas'], 'NY': ['Albany', 'Syracuse', 
    # 'Buffalo', 'Rochester'], 'CA': ['Sacramento', 'Palo Alto'], 'GA': ['Atlanta']})
print() # Blank line

print("Here are the formatted results:")
for state, cities in cities_by_state.items(): 
    # IMPORTANT: Using 'items' keeps elements in the state whole, 
    # otherwise WITHOUT IT, the state wll be broken up into 2 characters 
    # in the following print statement, and you won't pick up the cities !!!
    
    print(state,"cities are:",'/'.join(sorted(cities))) 
        # '/'.join(cities) will remove the the formatting
        # and use a 'slash' or whatever you use to separate the cities.
        # I added a secondary sort to the cities in cities_by_state per state

# Output will look like this - just what we wanted!

# Here are the formatted results:
# AK cities are: Fairbanks/Homer/Valdez
# CA cities are: Palo Alto/Sacramento
# CO cities are: Denver/Greeley/Pueblo
# GA cities are: Atlanta
# MN cities are: St. PAUL
# NY cities are: Albany/Buffalo/Rochester/Syracuse
# TX cities are: Dallas/Georgetown/Houston

print() # Blank line
print("YAY - I hope this helped you!")    

  


