name = "Henry"
ageHP= 15
ageBS = 17
ageBA = 15
ageDN = 16
x = 3
y = 7
z = x * y
sum = x + y

print("Hello World!")
print("Hello", name)
print("Name:", name, "Age:", ageHP)

print ("x:", x)
print ("y:", y)
print ("z:", z)
print ("Sum:", sum)

print("Average age of some people I know:", (ageHP + ageBS + ageBA + ageDN) / 4)

print(range(ageHP))
print(range(89,22,1))

for i in range(1, ageDN+1, 1):
    print(i)

def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break




# Sample list to be sorted
arr = [6,6,2]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array:", data)

sorted_data = quicksort(data)
print("Sorted Array:", sorted_data)