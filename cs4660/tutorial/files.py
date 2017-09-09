"""Files tests simple file read related operations"""
from io import open
import lists
import files
from tutorial import lists

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)"""

        sf = open(file_path, "r")
        if sf.mode =='r':
            fil = sf.readlines()
            for x in fil:
                data = x.split()
                values = []
                for i in data:
                    values.append(int(i))
                self.numbers.append(values)
    

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        values= self.numbers[line_number]
        return sum(values)/float(len(values))

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        values= self.numbers[line_number]
        return max(values)
    pass

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        values= self.numbers[line_number]
        return min(values)
    pass

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        values= self.numbers[line_number]
        return sum(values)
    pass
