
import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    
display_main_menu()

def get_user_input():
    user_input=input()
    user_split=user_input.split(",")
    numbers = [float(num) for num in user_split if num.strip()]# Filter out empty strings
    print(numbers)
    return numbers

def calc_average(numbers):
   # print("calc_average=")
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)



def find_min_max(numbers):
    if not numbers:
        return [None, None]
    return [min(numbers), max(numbers)]


# Get user input
numbers = get_user_input()

# Calculate the average
average = calc_average(numbers)

# Calculate the minimum and maximum values
min_max = find_min_max(numbers)

# Print the results
print("Average:", average)
print("Minimum:", min_max[0])
print("Maximum:", min_max[1])

def calc_average_temperature(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calc_min_max_temperature(numbers):
    if not numbers:
        return [None, None]
    return [min(numbers), max(numbers)]

sorted_numbers= sorted(numbers)

def calc_median_temperature(sorted_number):
    n = len(sorted_numbers)
    if n == 0:
        return None  # Handle the case where the list is empty
    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle one
        return sorted_numbers[n // 2]
    else:
        # If the list has an even number of elements, return the average of the two middle ones
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2


pos=calc_median_temperature(sorted_numbers)
median=calc_median_temperature(sorted_numbers)

#tempmax=def calc_min_max_temperature(numbers)
minmaxtemp=calc_min_max_temperature(numbers)
avgtemp=calc_average_temperature(numbers)

print("min temp:",minmaxtemp[0])
print("max temp:",minmaxtemp[1])
print("avg temp:",avgtemp)
print("median temp:",median) #statistics.median(numbers))