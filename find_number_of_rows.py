def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    s=0
    column_name=data.split()
    
    
    
    
    return len(column_name)

data = open('data.csv').read()
print(find_number_of_rows(data))
    
  

# Read the csv file
