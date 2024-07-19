import numpy as np

def create_max():
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of columns: "))
    
    arr5 = []
    
    for i in range(row):
        rows = []
        for j in range(col):
            value = int(input(f"Enter value at ({i},{j}): "))
            rows.append(value)
        arr5.append(rows)

    arr5 = np.array(arr5)
    return arr5

us = create_max()
print("Array created:")
print(us)

    

#arr1=np.array([[1,32,3,4,5,6,7],[14,32654,354,44,54,66,47]])
#arr2=np.array([1,32,3,4,5,6,7])
#arr3 = arr1+arr2
#print(arr3[0,3])


arr4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n",arr4[0,0]," ",arr4[0,1]," ",arr4[0,2],"\n",arr4[1,0]," ",arr4[1,1]," ",arr4[1,2],"\n",arr4[2,0]," ",arr4[2,1]," ",arr4[2,2],"\n",)

        

