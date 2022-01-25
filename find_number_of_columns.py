def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    column_name=data.split()    
    return len(column_name[0].split(","))

data = open('data.csv').read()
print(find_number_of_columns(data))

    
    

# Read the csv file