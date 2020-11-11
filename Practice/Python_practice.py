# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


# for county in counties_dict:
#     print(county)

# #only returns the values
# for county in counties_dict.values():
#     print(county)

# #only returns the values
# for county in counties_dict:
#     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(county, "county has", voters, "registered voters.")

#################

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)


# #to retrieve values from each dictionary in dictionary list
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# #registered voters in each dictionary
# for county_dict in voting_data:

#      print(county_dict['registered_voters'])


# #print only the county name
# for county_dict in voting_data:
#     print(county_dict['county'])
#  # the variable county_dict could be any variable and works if just 'i'

####################

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#####################
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
