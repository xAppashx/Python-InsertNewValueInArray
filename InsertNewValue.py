
#We want to insert a new value in a sorted array,
#But we want the array to stay sorted

# This function inserts the new value in the correct spot of the array
# Independently whether the array is Ascending or Decending sorted

def InsertNewValue(Array, Value): 
      
      #We verify if the array is ascending or decending sorted
      lenArray = len(Array)
      SortMethod = True # True for Ascending, False for Decending
      
      if (Array[0] > Array[lenArray - 1]): 
            SortMethod = False
      #if
      
      
      #We create a new spot in the Array and we set it as None
      Array.append(None)
      
      
      if (SortMethod == True): #SortMehod is Ascending
      
            #We place None where the Value should go
            Pivot = lenArray
            while (Array[Pivot - 1] != None) and (Array[Pivot - 1] > Value): 
                  
                  Array[Pivot] = Array[Pivot - 1]
                  Array[Pivot - 1] = None
                  Pivot = Pivot - 1
                  
                  if (Pivot == 0): 
                        break
                  #if
                  
            #while
            
            # We insert the Value where None was placed
            Array[Pivot] = Value
      #if (SortMehod == 0) 
      
      
      else: #if SortMethod is Decending
            
            #We place None where the Value should go
            Pivot = lenArray
            while (Array[Pivot - 1] != None) and (Array[Pivot - 1] < Value): 
                  
                  Array[Pivot] = Array[Pivot - 1]
                  Array[Pivot - 1] = None
                  Pivot = Pivot - 1
                  
                  if (Pivot == 0): 
                        break
                  #if
                  
            #while
            
            # We insert the Value where None was placed
            Array[Pivot] = Value
      #else
      
      
      return (Array)
      
#def InsertNewValue




# Test of the use of the function.

# We start with a ascending sorted array and we want to insert the value 4
# Whilst maintaining the array sorted
Array = [1, 2, 3, 5, 6, 7]
ValueToInsert = 4

print("Ascending sorted array: ", Array)
print("Value to insert: ", ValueToInsert)

Array = InsertNewValue(Array, ValueToInsert)

print("Final array: ", Array)

print("\n")



#Secound case, decending sorted array: 
#This time we insert the value 7
Array = [9, 8, 6, 5, 4, 3]
ValueToInsert = 7

print("Decending sorted array: ", Array)
print("Value to insert: ", ValueToInsert)

Array = InsertNewValue(Array, ValueToInsert)

print("Final array: ", Array)

