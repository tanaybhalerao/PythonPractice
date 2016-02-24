# Code written in Python 3.5
"""
Modules:
1)random: Implements pseudo-random number generator.
2)requests: Helps in integration with web services
3)datetime: Manipulating dates
4)csv: Read and write tabular data in CSV format
"""
import random
from datetime import date
import csv
import requests


class Aya:
    """
    This class has methods to:
    1)Build columns
    2)Generate an index
    3)Generate gaussian distribution
    4)Generate random words(English Dictionary)
    5)Write as a tab delimited file

    """

    def __init__(self, num_of_elements, norm_columns, str_columns):
        """
        Initializing variables for:
        1) Total no. of data points
        2) Total no. of columns having gaussian distribution of random numbers
        3) Total no. of columns having random English dictionary strings

        """
        self.total_records = num_of_elements+1
        self.gauss_cols = norm_columns
        self.char_cols = str_columns
        self.gauss_cols_list = self.generate_columns(norm_columns)
        self.char_cols_list = self.generate_columns(str_columns)
        self.website = 'http://svnweb.freebsd.org/csrg/share/dict/words' \
                       '?view=co&content-type=text/plain'

    @classmethod
    def generate_columns(cls, num_of_cols):
        """
        Used for generating col2 to col10 and col11 to col19
        num_of_cols: The number of lists created within a list(used as columns)
        Returns empty list of lists(creates structure)

        """
        cols = [[] for _ in range(num_of_cols)]
        return cols

    def generate_sequence(self):
        """
        Generates the index column(col1)

        """
        col = [idx for idx in range(1, self.total_records)]
        col.insert(0, "col1")
        return col

    def generate_norm(self):
        """
        Generates random dataset with a normal distribution at different means.
        It has 10% null values

        """
        mean_header = []

        for i in range(self.gauss_cols):

            random.seed(i)
            mean = random.randint(i, i+10)
            std = random.randint(i, i+5)

            for j in range(1, self.total_records):
                if j <= int(0.9*self.total_records):
                    norm = random.gauss(mean, std)
                    self.gauss_cols_list[i].append(norm)
                else:
                    self.gauss_cols_list[i].append('')

            without_null = [item for item in
                            self.gauss_cols_list[i] if item != '']

            try:
                mean_value = sum(without_null)/len(self.gauss_cols_list[i])
                mean_header.append(mean_value)
            except ZeroDivisionError:
                mean_header.append('ERROR')
                print('Division by zero. Appending column '+str(i+2) +
                      ' with ERROR. Please check inputs')

            self.gauss_cols_list[i].insert(0, ("col" +
                                               str(i+2) +
                                               "_" +
                                               str(mean_header[i])))

        return self.gauss_cols_list

    def generate_string(self):
        """
        Generates random words extracted from the website.

        """
        web_open = requests.get(self.website)
        wordlist = web_open.content.split()

        for i in range(self.char_cols):
            for j in range(1, self.total_records):
                if j <= int(0.9*self.total_records):
                    self.char_cols_list[i].append(random.choice(wordlist))

                else:
                    self.char_cols_list[i].append('')

            self.char_cols_list[i].insert(0, "col" + str(i+2+self.gauss_cols))

        return self.char_cols_list

    def generate_date(self):
        """
        Generates random dates between January 1,2014 and December 31,2014

        """
        col = []
        start_date = date(day=1, month=1, year=2014).toordinal()
        end_date = date(day=31, month=12, year=2014).toordinal()
        for _ in range(self.total_records):
            random_day = date.fromordinal(random.randint(start_date, end_date))
            col.append(str(random_day))

        col.insert(0, "col"+str(self.char_cols+self.gauss_cols+2))

        return col

    def write_csv(self):
        """
        This function writes the data to a tab delimited file

        """
        url = "C:\\Users\\Tanay\\Documents\\Interview\\aya_assignment.csv"
        with open(url, "w", newline='') as handle_open:
            writer = csv.writer(handle_open, delimiter='\t')
            for i in range(self.total_records):
                writer.writerow([x[i] for x in LIST_FINAL])


TOTAL_INPUT = input("Enter the no. of records to generate: ")
NORM_INPUT = input("Enter the no. of columns having gaussian distribution: ")
STR_INPUT = input("Enter the no. of columns with random English words: ")

# Creating object of the class with the above parameter
# Exceptions handle invalid inputs

try:
    AYA = Aya(int(TOTAL_INPUT), int(NORM_INPUT), int(STR_INPUT))
except ValueError:
    print("Please enter an appropriate number")

# Generating different columns of the data set

COL_1 = [AYA.generate_sequence()]
COL_2 = AYA.generate_norm()
COL_3 = AYA.generate_string()
COL_4 = [AYA.generate_date()]

# Combining the columns into a single data set

LIST_FINAL = COL_1 + COL_2 + COL_3 + COL_4

# Writing the data set to disk as tab separated file.

AYA.write_csv()
