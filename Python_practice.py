print ("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
    print(counties[2])



counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El PAso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print ("Arapahoe or El PAso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
for county in counties:
    print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county_dict in voting_data:
    for value in county_dict .values():
        print(value)

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
