import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

from preprocspectra import make_average


class TestMakeAverage(unittest.TestCase):
  def test_structure(self):
    # Test if structure of output is correctly and if the function return the average of values
    
    df = pd.DataFrame({'id': [1, 2, 3, 4], 'chemical': [2.91, 2.91, 3.01, 3.01], 1: [3.0, 5.0, 2.0, 1.0], 2: [4.0, 8.0, 4.0, 3.0], 3: [2.0, 2.0, 4.0, 2.5], 4: [3.0, 7.0, 8.0, 6.0]})
    df.index = [0,1,2,3]
    expected = pd.DataFrame({'id': [1, 3], 'chemical': [2.91, 3.01], 1: [4.0, 1.5], 2: [6.0, 3.5], 3: [2.0, 3.25], 4: [5.0, 7.0]})
    expected.index = [0,2]
    result = make_average(df, 2, 2)

    assert_frame_equal(result, expected)
  
  def test_input_values(self):
    # Test if the function handle with invalid params
    df = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], 1: [3.0, 5.0], 2: [4.0, 8.0], 3: [2.0, 2.0], 4: [3.0, 7.0]})
    test1 = 'test'
    test2 = 0
    test3 = True

    self.assertRaises(ValueError, make_average, test1, 2, 2)
    self.assertRaises(ValueError, make_average, test1, 2, test1)
    self.assertRaises(ValueError, make_average, test2, 2, test2)
    self.assertRaises(ValueError, make_average, test3, 2, test3)
