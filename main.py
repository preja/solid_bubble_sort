# Define a function to create the sorting and pass in an array as the parameter
def bubble_sort(arr):
    # Get the length of the array
    arr_len = len(arr)
    # Loop through the array to access the elements in it, including the last one - outer loop
    for i in range(arr_len-1):
        # declare a flag variable to check if a swap has occured - for optimization
        flag = 0
        # create a loop to compare each element of the array till the last one
        for j in range(0, arr_len-i-1):
            # compare 2 adjacent elements and sort them in ascending order
            if arr[j] > arr[j+1]:
                # Swap the elements if they are not in the right order
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                # break out of the loop at 0
                if flag == 0:
                    break
    # return value must be in the outer loop block
    return arr


arr = [5, 3, 4, 1, 2]
print("List sorted with bubble sort in ascending order: ", bubble_sort(arr))
#solid style verison without optimalization

set_to_sort = [5, 3, 4, 1, 2]
def get_length() -> int:
    return len(set_to_sort)

def is_swap_needed(currnt_element_index: int) -> bool:
    return set_to_sort[currnt_element_index] > set_to_sort[currnt_element_index+1]

def swap_two_elements_by_index(currnt_element_index: int, next_element_index:int) -> None:
      set_to_sort[currnt_element_index], set_to_sort[next_element_index] = set_to_sort[next_element_index], set_to_sort[currnt_element_index]

def swap(currnt_element_index:int):
    swap_two_elements_by_index(currnt_element_index, currnt_element_index+1)
      
def bring_the_greatest_element_to_the_end_of_set(iteration_number):
    current_subset_length = get_length()-iteration_number-1
    for j in range(0, current_subset_length):
        if is_swap_needed(j):
            swap(j)
    print(set_to_sort);       
        
def bubble_sort_solid():
    for iteration_number in range(0, get_length()-1):
        bring_the_greatest_element_to_the_end_of_set(iteration_number)
   
    

print("List sorted with bubble sort solid in ascending order: ", set_to_sort())


# Output: List sorted with bubble sort in ascending order:  [1, 2, 3, 4, 5]
