"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        f = open(".cs4660/test/fixtures/array.txt")
        data = f.read()
        text = data.decode('utf-8')
        array = []
        for line in ins:
            line = line/rstrip('\n')
            array.append(line)
            ins.close()
            print array

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        return sum(array)/2

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
       return max(array)

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
       return min(array)

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
       return sum(array)
