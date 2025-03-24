from itertools import count
import unittest

from DataLoader import *

class LoadDataTestCase(unittest.TestCase):

    def test_0_getDataFromDir(self):
        data = getDataFromDir("UnitTestData/Data/Class1/", "Class1")
        self.assertEqual(len(data), 2)
        for labeledImage in data:
            self.assertEqual(labeledImage[0], "Class1")

    def test_1_getDataFromDir(self):
        data = getDataFromDir("UnitTestData/SplitData/Test/Class2/", "Class2")
        self.assertEqual(len(data), 2)
        for labeledImage in data:
            self.assertEqual(labeledImage[0], "Class2")

    def test_2_getNumOfClasses(self):
        self.assertEqual(getNumOfClasses("UnitTestData/Data"), 3)

    def test_3_getNumOfImages(self):
        self.assertEqual(getNumOfImages("UnitTestData/SplitData/Train"), 9)

    def test_4_getData(self):
        data = getData("UnitTestData/Data/")
        self.assertEqual(len(data), 8)

    def test_5_getDataFromSplit(self):
        data = getDataFromSplit("UnitTestData/SplitData/")
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data[0]), 9)
        self.assertEqual(len(data[1]), 6)
        self.assertEqual(len(data[2]), 4)

    def test_6_getSplitData(self):
        # Hard to test on a small dataset because of percentages
        data = getSplitData("UnitTestData/Data/")
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data[0]), 5)
        self.assertEqual(len(data[1]), 1)
        self.assertEqual(len(data[2]), 2)
        
    def test_7_getSplitData(self):
        # Using real dataset with 3k images
        data = getSplitData("Data/Animals/")
        self.assertEqual(len(data), 3)
        self.assertEqual(len(data[0]), 2103)
        self.assertEqual(len(data[1]), 601)
        self.assertEqual(len(data[2]), 301)

    