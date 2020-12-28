counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
#For Loop List examples    
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

#Tuple examples
for county in counties_tuple:
    print(county)

for i in range(len(counties_tuple)):
    print(counties_tuple[i])

#For loops over dictionaries

## To only get the KEYS
for county in counties_dict:
    print(county)

for county in counties_dict: #returns values
    print(counties_dict[county])

# Get() method returns values of the keys
for county in counties_dict:
    print(counties_dict.get(county))

#keys() method, variable name does not matter. keys will be printed in order
for county in counties_dict.keys():
    print(county)

# values() method, again variable name does not matter
for voters in counties_dict.values():
    print(voters)

# getting the both the key and value pairs . items() method
#because the key and value variables were previously metioned they can be called in this fashion
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, "county has", voters,"registered voters.")

# itirating through multiple dictionaries. Use the range() method
for i in range(len(voting_data)):

      print(voting_data[i])

#Get values from a list of dictionaries use a nested for loop

for county_dict in voting_data: #retrieving each dictionary
    for value in county_dict.values(): # retrieving the values from each dictionary
        print(value)

#retrieving the registered voters from each dictionary
for county_dict in voting_data:
     print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county']) #only the county name

#PRINTING FORMATS**********************************************************

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. " #notice the comma
    f"The total number of votes in the election was {total_votes:,}. " #notice the comma
    f"You received {candidate_votes / total_votes * 100:.2f} % of the total votes.") #the precision of decimal places
print(message_to_candidate)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I recieved {my_votes / total_votes * 100}% of the total votes")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

### multiline F-strings ***********

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)