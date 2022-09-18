import numpy as np

# Fetching data from User
while True:
    try:
        
        array_1 = np.array(list(map(int,input("\nPlease Provide me Array 1 with space( ) seperator: ").strip().split())))
        array_2 = np.array(list(map(int,input("\nPlease provide me Array 2 with space( ) seperator: ").strip().split())))
        break

    except:
        print("\n\nWarning:Only integer are accepted:")
        
def medianarray(array1, array2):
    # I can directly use np.median function to find median but I develop my own logic
    array = np.concatenate((array1,array2), axis=0) #Merging bith arrays
    
    sort_array = np.sort(array) # Sorting the array
    
    center_index = len(sort_array)//2 # Getting the centered Rounded off index
    
    if not len(sort_array) % 2: # If remainder of 2 is not zero
        median = (sort_array[center_index - 1] + sort_array[center_index]) / 2.0
    else: # If remainder of 2 is zero
        median = sort_array[center_index]
    
    
    print(f"The median of both concatenated array {array} is {median}.")
    
medianarray(array_1, array_2)