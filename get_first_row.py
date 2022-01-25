from find_number_of_columns import find_number_of_columns


def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   column_name=data.split()    
   return column_name[1].split(",")

data = open('data.csv').read()
print(get_first_row(data))

# Read the csv file