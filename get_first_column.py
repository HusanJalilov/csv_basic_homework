def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    s=[]
    idx=0
    column=data.split('\n')
    for i in column:
        list1=column[idx].split(',')
        s.append(list1[0])
        idx+=1
        
    
    return s

    
data=open("data.csv").read()
print(get_first_column(data))
    
    
    
# Read the csv file