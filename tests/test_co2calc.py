import unittest
import sys
sys.path.append('..')
from myco2cli.funcmodule import co2calc
import click
import json

import os
import subprocess

with open('../emissions.json','r') as f:
    co2emissions = json.load(f)

class TestCO2Calc(unittest.TestCase):

    # test CO2eq calculations
    def test_default(self):
        self.assertEqual(co2calc(co2emissions['medium-diesel-car'], \
        15,'km','na')[0],2.6)
        self.assertEqual(co2calc(co2emissions['train'], 14500,'m',\
        'na')[0],87)
        self.assertEqual(co2calc(co2emissions['large-petrol-car'], \
        1800.5,'km','na')[0],507.7)
        self.assertEqual(co2calc(co2emissions['train'], 14500,'m',\
        'kg')[0],0.1)
        self.assertEqual(co2calc(co2emissions['train'], 14,'km',\
        'kg')[0],0.1)
        self.assertEqual(co2calc(co2emissions['train'], 14,'km',\
        'g')[0],84)
        self.assertEqual(co2calc(co2emissions['train'], 1400,'m',\
        'g')[0],8.4)

    # test default output unit for distance unit==km
    def test_default_output_kg(self):
        self.assertEqual(co2calc(co2emissions['medium-diesel-car'],\
        15,'km','na')[1],'kg')
        self.assertEqual(co2calc(co2emissions['large-petrol-car'],\
        1800.5,'km','na')[1],'kg')

    # test default output unit for distance unit==km and distance unit==m
    def test_default_output_g(self):
        self.assertEqual(co2calc(co2emissions['train'],14500,'m',\
        'na')[1],'g')
        self.assertEqual(co2calc(co2emissions['medium-diesel-car'],\
        24500,'m','na')[1],'g')

if __name__=='__main__':
    unittest.main(buffer=True)
