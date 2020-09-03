import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pandas.testing import assert_frame_equal
from preprocspectra.transformation_tools import snv, msc, area_norm, plus_sg
import unittest
import pandas as pd
import numpy as np

class TestTransformation(unittest.TestCase):
    def test_snv(self):
        spectra_start = 2
        df = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [3.0, 5.0], '2': [4.0, 8.0], 3: [2.0, 2.0], 4: [3.0, 7.0]})
        df_result = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [0, -0.188982236504614], '2': [1.22474487128318, 0.944911182523068], 3: [-1.22474487128318, -1.3228756555323], 4: [0, 0.566946709513841]})
        result = snv(df, spectra_start)

        test1 = 'Test'
        test2 = 2
        test3 = True

        self.assertRaises(ValueError, snv, test1, spectra_start)
        self.assertRaises(ValueError, snv, test2, spectra_start)
        self.assertRaises(ValueError, snv, test3, spectra_start)
        self.assertRaises(ValueError, snv, df, test1)


        assert_frame_equal(result, df_result)
    
    
    def test_area_norm(self):
        spectra_start = 2
        df = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [3.0, 5.0], '2': [4.0, 8.0], 3: [2.0, 2.0], 4: [3.0, 7.0]})
        df_result = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [0.25, 0.227272727272727], '2': [0.333333333333333, 0.363636363636364], 3: [0.166666666666667, 0.0909090909090909], 4: [0.25, 0.318181818181818]})
        result = area_norm(df, spectra_start)

        test1 = 'Test'
        test2 = 2
        test3 = True

        self.assertRaises(ValueError, area_norm, test1, spectra_start)
        self.assertRaises(ValueError, area_norm, test2, spectra_start)
        self.assertRaises(ValueError, area_norm, test3, spectra_start)
        self.assertRaises(ValueError, area_norm, df, test1)

        assert_frame_equal(result, df_result)
    

    def test_msc(self):
        spectra_start = 2
        df = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [0.065531, 0.078001], '2': [0.065424, 0.077883], '3': [0.06535, 0.07780], '4': [0.065331, 0.077761]})
        df_resutlt = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [0.07176754, 0.07176469], '2': [0.07165141, 0.07165529], '3': [0.07157109, 0.07157834], '4': [0.07155047, 0.07154218]})
        result = msc(df, spectra_start)

        test1 = 'Test'
        test2 = 2
        test3 = True

        self.assertRaises(ValueError, msc, test1, spectra_start)
        self.assertRaises(ValueError, msc, test2, spectra_start)
        self.assertRaises(ValueError, msc, test3, spectra_start)
        self.assertRaises(ValueError, msc, df, test1)

        assert_frame_equal(result, df_resutlt)

    
    def test_plus_sg(self):
        
        df = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [3.0, 5.0], '2': [4.0, 8.0], '3': [2.0, 2.0], '4': [3.0, 7.0]})
        df_averaged = pd.DataFrame({'id': [1, 2], 'chemical': [2.91, 2.91], '1': [0.25, 0.227272727272727], '2': [0.333333333333333, 0.363636363636364], '3': [0.166666666666667, 0.0909090909090909], '4': [0.25, 0.318181818181818]})

        self.assertRaises(ValueError, plus_sg, 'test', 'test', 'test', 'test', 'test', 'test', 2)
