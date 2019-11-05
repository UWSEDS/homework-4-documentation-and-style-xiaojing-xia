"""
This module provides the functions to test a dataframe.
"""
import unittest
import pandas as pd

# Load data from url.
URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
DF = pd.read_csv(URL)
(ROW, COLUMN) = DF.shape # Get the row and column numbers of the dataframe

class UnitTests(unittest.TestCase):
    """
    This class includes 6 tests.
    The first 3 tests are the same as homework2.
    The last 3 tests are new tests from homework3.
    """
    def test_hm2_length(self):
        """
        This function tests if the dataframe has at least 10 rows.
        The input is a dataframe.
        It returns True / False.  If the dataframe has more than 10 lines, return True.
        """
        self.assertTrue(ROW >= 10)

    def test_hm2_name(self):
        """
        This function tests if the column names in the datafram are the same as
        the name list provided in the following codes.
        The input is a dataframe.
        It returns True / False.
        If all the cloumn names match the namelist, return True.
        """
        is_true = True
        column_name = ["Date", "Fremont Bridge East Sidewalk", "Fremont Bridge West Sidewalk"]
        for i in range(0, COLUMN):
            if DF.columns[i] not in column_name:
                is_true = False
        self.assertTrue(is_true)
    def test_hm2_type(self):
        """
        This function tests if the data in each column has the same type.
        The input is a dataframe.
        It returns True / False.
        If every cloumn has the same data type, return True.
        """
        temp = 1
        for column_m in range(0, COLUMN):
            if temp == 0:
                break
            for row_n in range(0, ROW-1):
                if type(DF[DF.columns[column_m]][row_n]) != type(DF[DF.columns[column_m]][row_n+1]):
                    temp == 0
                    break
        self.assertTrue(temp)
    def test_correct_type(self):
        """
        This function tests if data in columns are "str", "float", and "float".
        The input is a dataframe.
        It returns True / False.
        If each column's data have the same type, and satisfies the given type, return True.
        """
        column_type = ["str", "float64", "float64"]
        temp = 1
        for column_m in range(0, COLUMN):
            if temp == 0:
                break
            for row_n in range(0, ROW-1):
                if type(DF[DF.columns[column_m]][row_n]) != type(DF[DF.columns[column_m]][row_n+1]):
                    temp == 0
                    break
            if temp:
                if type(DF[DF.columns[column_m]][0]).__name__ != column_type[column_m]:
                    temp = 0
        self.assertTrue(temp)
    def test_nan(self):
        """
        This function tests if the dataframe has null value.
        """
        self.assertTrue(DF.isnull().values.any())
    def test_one(self):
        """
        This function tests if there is at least one line of data.
        """
        self.assertTrue(ROW >= 1)
SUITE = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(SUITE)
