counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict:
    print(county)

#only returns the values
for county in counties_dict.values():
    print(county)

#only returns the values
for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


#to retrieve values from each dictionary in dictionary list
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#registered voters in each dictionary
for county_dict in voting_data:

     print(county_dict['registered_voters'])


#print only the county name
for county_dict in voting_data:
    print(county_dict['county'])
 # the variable county_dict could be any variable and works if just 'i'

