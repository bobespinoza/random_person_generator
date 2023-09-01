#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
"""
Created on Sun Jul 16 19:31:54 2023

@author: Espinoza_MacBookPro
"""

import statistics
from statistics import variance
from statistics import stdev

class TddRefactor:
    def __init__(self):
        pass

    def read_ints(self, file):
        self.file = file
        int_list = []
        with open(file, 'r') as f:
            for num in f:
                int_list.append(int(num.strip()))
        return int_list
 
    def count(self, list):
        self.list = list
        return len(self.list)
   
    def summation(self, list):
        self.list = list
        list_sum = 0
        for num in self.list:
            list_sum += num
        return list_sum
   
    def list_average(self, list):
        self.list = list
        total = self.summation(list)
        list_avg = round(total/len(list))
        return list_avg
    def list_min(self, list):
        self.list = list
        list_min = 10000
        for num in self.list:
            if list_min > num:
                list_min = num
        return list_min
    def list_max(self, list):
        self.list = list
        list_max = 0
        for num in self.list:
            if list_max < num:
                list_max = num
        return list_max

    def list_harmonic(self, list):
        list_recip = []
        self.list = list
        list_count = self.count(list)
        for num in self.list:
            list_recip.append(1/num)
        total = self.summation(list_recip)
        list_harm = round(list_count/total)
        return list_harm

    def list_variance(self, list):
        self.list = list
        return round(variance(self.list))

    def list_stdev(self, list):
        self.list = list
        return round(stdev(self.list))
 
 
def compute_stats(file):
    a = TddRefactor()
    int_list = a.read_ints(file)
    print(f'Count = {a.count(int_list)}')
    print(f'Summation = {a.summation(int_list)}')
    print(f'Average = {a.list_average(int_list)}')
    print(f'Minimum = {a.list_min(int_list)}')
    print(f'Maximum = {a.list_max(int_list)}')
    print(f'Harmonic mean = {a.list_harmonic(int_list)}')
    print(f'Variance = {a.list_variance(int_list)}')
    print(f'Standard deviation = {a.list_stdev(int_list)}')
 
if __name__ == '__main__':
    compute_stats('random_nums.txt')
    
 
