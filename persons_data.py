import csv
import random
from typing import List
from dataclasses import dataclass

from faker import Faker
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    email: str


def persons_from_csv() -> List[Person]:
    result: List[Person] = []

    with open('test-data/Persons.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row)
            person = Person(
                first_name=row['First name'],
                last_name=row['Last name'],
                age=int(row['Age']),
                email=row['Email']
            )
            result.append(person)
    return result


def persons_from_excel() -> List[Person]:
    # Задаем пустой список, где будем хранить объекты класса Person
    persons: List[Person] = []

    # Открываем Excel-файл.
    workbook: Workbook = load_workbook(
        filename='test-data/Persons.xlsx',
        read_only=False
    )

    # По индексу получаем ссылку на первую вкладку.
    first_sheet: Worksheet = workbook.worksheets[0]

    # Ковертируем значения из объектов класса Cell в базовые типы Python: str, int.
    datarows = []
    for row in first_sheet.rows:
        # Каждый рядок — это кортеж (tuple) где каждый элемент — класс Cell.
        values: List = [cell.value for cell in row]
        datarows.append(values)

    # Аллоцируем оъекты класса Person для каждой строчки Эксель-файла, кроме первой (т. к. это заголовок).
    for values in datarows[1:]:
        person = Person(
            first_name=values[0],
            last_name=values[1],
            age=values[2],
            email=values[3]
        )
        persons.append(person)

    return persons


def random_person(count: int) -> List[Person]:

    persons: List[Person] = []

    fake = Faker(locale='ru_RU')

    for _ in range(count):
        person = Person(
            first_name=fake.first_name_male(),
            last_name=fake.last_name_male(),
            age=random.randrange(18, 50),
            email=fake.email()
        )
        persons.append(person)

    return persons
