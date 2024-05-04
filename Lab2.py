def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    user_input=input()
    user_split=user_input.split(",")
    numbers = [float(num) for num in user_split]   
    return(numbers)
def find_min_max(numbers):
    return [min(numbers), max(numbers)]

def calc_average(numbers): 
    return [sum(numbers) / len(numbers)]
def calc_median_temperature(numbers):
    sorted_data = sorted(numbers)
    n = len(sorted_data)
    if n % 2 == 0:
        medim = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        medim = sorted_data[n // 2]
    return (medim)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu() 
    num_list = get_user_input() 
    print(find_min_max(num_list))
    print(calc_average(num_list))
    print(calc_median_temperature(num_list))
    
if __name__ == "_main_":
    main()