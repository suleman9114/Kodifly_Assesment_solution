import numpy as np

constraints = "\nPlease follow these Constraints \nThe number of nodes in the list is sz. \n1 <= sz <= 30 \n0 <= Node.val <= 100 \n1 <= n <= sz"
print(constraints)


while True:
    try:
        
        node_array = np.array(list(map(int,input("\nPlease provide me the number List with space( ) seperator: ").strip().split())))
        node_index = int(input("Please tell us which index of node you want to remove from end (Single Number): "))
        if ((np.any(node_array>100)) or (np.any(node_array<0)) or (node_array.size>30) or (node_array.size<1) or node_index<1 or (node_index>(node_array.size))):
            print(f"\n\nPlease Follow the Constraints \n\n{constraints}")
        else:
            break
    except:
        print("\n\nWarning:You are missing something, Only integer are accepted and only single number is accepted for second input:")
            
    
    
# rev_node_array = node_array[::-1]
output = np.delete(node_array, -node_index)

print("The Output Array is: ", output)
