from address_data import addresses_from_csv
from persons_data import persons_from_csv, persons_from_excel, random_person

print("Персоны из CSV:")
for person in persons_from_csv():
    print(person)

print("Персоны из Excel:")
for person in persons_from_excel():
    print(person)


print("10 вымышленных персон:")
for person in random_person(10):
    print(person)

for address in addresses_from_csv():
    print(address)

