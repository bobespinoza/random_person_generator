#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 2024

@author: Espinoza_MacBookPro
"""


import unittest
from random_person_generator import TddRandomPerson

class TestTddRandomPerson(unittest.TestCase):


    def test_read_male_first_name(self):
        male_name = TddRandomPerson()
        file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.male.first'
        self.assertEqual(male_name.read_name(file)[0], 'JAMES')

    def test_read_female_first_name(self):
        female_name = TddRandomPerson()
        file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.female.first'
        self.assertEqual(female_name.read_name(file)[0], 'MARY')

    def test_read_surname(self):
        surname = TddRandomPerson()
        file = '/Users/Espinoza_MacBookPro/Desktop/Python/project/random_person/dist.all.last'
        self.assertEqual(surname.read_name(file)[0], 'SMITH')

    def test_generate_random_email_service(self):
        service = TddRandomPerson()
        self.assertEqual(service.generate_random_email_service(1), 'gmail')

    def test_generate_random_phone_number(self):
        phone = TddRandomPerson()
        self.assertEqual(phone.generate_random_phone_number(231, 456, 7890), '231-456-7890')

    def test_generate_random_age(self):
        age = TddRandomPerson()
        self.assertEqual(age.generate_random_age(90), 90)

    def test_generate_occupation_under_four(self):
        occupation = TddRandomPerson()
        self.assertEqual(occupation.generate_random_occupation(1, 1), 'N/A')

    def test_generate_occupation_between_four_and_18(self):
        occupation = TddRandomPerson()
        self.assertEqual(occupation.generate_random_occupation(6, 1), 'Student')

    def test_generate_occupation_adult(self):
        occupation = TddRandomPerson()
        self.assertEqual(occupation.generate_random_occupation(19, 1), 'Actor')



if __name__ == '__main__':
    unittest.main()
 
