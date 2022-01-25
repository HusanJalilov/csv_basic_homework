def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    clounm_name = data.split('\n')
    return len(clounm_name)-1

data = open('data.csv').read()
print(find_number_of_rows(data))
    
  

# Read the csv file
