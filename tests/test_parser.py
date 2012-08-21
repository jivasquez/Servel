# -*- coding: utf-8 -*-
import os

import unittest
from servel.parser import Parser

class TestParser(unittest.TestCase):
    
    def setUp(self):
        self.antartica_filename = "%s/antartica.txt", os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.citizens = Parser.parse(self.antartica_filename)
    
    def test_number_of_citizens(self):
        self.assertEqual(367, len(self.citizens))
        
    def test_citizen_data(self):
        expected_citizen_1 = {
        'name': 'ABARCA GONZALEZ LUIS ENRIQUE',
        'run': '8407686-4',
        'sex': 'VAR',
        'address': 'VAR B A EDO FREI MONTALVA',
        'circumscription': 'ANTARTICA',
        'table': '3 V'
        }
        expected_citizen_70 = {
        'name': 'CAVIERES VALENZUELA NICOLAS ANDRES',
        'run': '15627218-3',
        'sex': 'VAR',
        'address': 'VAR B A EDO FREI M',
        'circumscription': 'ANTARTICA',
        'table': '3 V'
        }
        expected_citizen_100 = {
        'name': 'ESCOBAR VALDEBENITO RODRIGO GERARDO',
        'run': '10216892-5',
        'sex': 'VAR',
        'address': 'BASE PDTE FREI',
        'circumscription': 'ANTARTICA',
        'table': '2 V'
        }
        expected_citizen_286 = {
        'name': 'RODRIGUEZ SOLIS FRANCISCA JAVIERA',
        'run': '18725709-3',
        'sex': 'MUJ',
        'address': 'MANUEL ANTONIO MATTA BLOCK 0685 VILLA DEPTO . 206 RAUL SILVA HENRIQUEZ',
        'circumscription': 'ANTARTICA',
        'table': '2 V'
        }
        expected_citizen_367 = {
        'name': 'ZUÑIGA VIVANCO YANETH DE LOURDES',
        'run': '9714570-9',
        'sex': 'MUJ',
        'address': 'V LAS ESTRELLAS',
        'circumscription': 'ANTARTICA',
        'table': '1 M'
        }
        self.assertIn(expected_citizen_1, self.citizens)
        self.assertIn(expected_citizen_70, self.citizens)
        self.assertIn(expected_citizen_100, self.citizens)
        self.assertIn(expected_citizen_286, self.citizens)
        self.assertIn(expected_citizen_367, self.citizens)
        