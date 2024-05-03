#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 2024

@author: Espinoza_MacBookPro
"""

#male
#female
#surname
#service
#phone
#age
#occupation

#random_name
#random_person

import random

class TddRandomPerson:
    def __init__(self):
        pass

    def read_name(self, file):
        self.file = file
        name_list = []
        with open(file, 'r') as f:
            for name in f:
                name_list.append(name.split()[0])
        return name_list

    def generate_random_email_service(self, rand_num):
        email_service = ['aol', 'gmail', 'outlook', 'yahoo', 'icloud', 'yandex']
        return email_service[rand_num]

    def generate_random_phone_number(self, rand3nozero, rand3, rand4):
        phone_number = str(rand3nozero)+"-"+str(rand3)+"-"+str(rand4)
        return phone_number

    def generate_random_age(self, rand_age):
        age = int(rand_age)
        return age

    def generate_random_occupation(self, age, index):
        occupation_list = ['Cook', 'Actor', 'Programmer', 'Doctor', 'Dentist', 'Uber driver', 'Photographer', 'Astronaut']
        if (age > 0 and age < 5):
            return 'N/A'
        elif (age > 4 and age < 19):
            return 'Student'
        else:
            return occupation_list[index]

    def random_number_generator(self, minimum, maximum):
        return random.randint(minimum, maximum)

 
 
def generate_random_person():
    a = TddRandomPerson()


    rand_int = a.random_number_generator(1,2)

    if rand_int == 1:
        file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.male.first'
        first_name_list = a.read_name(file)
        sex = 'male'
    else:
        file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.female.first'
        first_name_list = a.read_name(file)
        sex = 'female'

    file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.all.last'
    surname_list = a.read_name(file)

    rand_int = a.random_number_generator(0,5)
    service = a.generate_random_email_service(rand_int)

    rand_int1 = a.random_number_generator(100,999)
    rand_int2 = a.random_number_generator(100,999)
    rand_int3 = a.random_number_generator(0,9999)
    phone = a.generate_random_phone_number(rand_int1, rand_int2, rand_int3)

    rand_int = a.random_number_generator(1,100)
    age = a.generate_random_age(rand_int)

    rand_int = a.random_number_generator(0,7)
    occupation = a.generate_random_occupation(age, rand_int)

    
    rand_int = a.random_number_generator(0,1000)
    first_name = first_name_list[rand_int]
    surname = surname_list[rand_int]
    print(first_name)
    print(surname)
    print(f'{first_name}.{surname}@{service}.com')
    print(phone)
    print(age)
    print(occupation)
    print(sex)
    
 
if __name__ == '__main__':
    generate_random_person()


 
