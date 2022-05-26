import csv
from dataclasses import dataclass
from typing import List


@dataclass
class Address:
    first_name: str
    last_name: str
    address_1: str
    city: str
    post_code: str
    country: str
    region_state: str


def addresses_from_csv() -> List[Address]:
    addresses: List[Address] = []

    with open('test-data/Addresses - Sheet1.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row)
            person = Address(
                first_name=row['First Name'],
                last_name=row['Last Name'],
                address_1=row['Address 1'],
                city=row['City'],
                post_code=row['Post Code'],
                country=row['Country'],
                region_state=row['Region / State']
            )
            addresses.append(person)

    return addresses