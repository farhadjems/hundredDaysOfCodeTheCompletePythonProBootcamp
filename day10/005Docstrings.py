# use ocstrings to create string for multi lines

string = '''Hello 
world!'''

print(string)


# use docstring to create documents for functions
def check_year(year):
    '''checks the given year whether is a leap year or not'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
