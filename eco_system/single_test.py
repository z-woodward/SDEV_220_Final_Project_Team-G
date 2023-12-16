""" 
@Program: single
@Author: Donald Osgood
@Last Date: 2023-12-10 20:10:10
@Purpose:Donald Osgood
"""
from engines import name_generator


class TestSuite(object):
    def __init__(self) -> None:
        pass
    def run_generator_test(self):
        """ name generator test
        """        
        res_generator = name_generator.RestaurantNameGenerator()
        value = res_generator.get_one_word("", "", "")
        print(value)

if __name__ == "__main__":
    test_suite = TestSuite()
    test_suite.run_generator_test()
