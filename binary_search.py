
def binary_search(list_of_num, num_to_search):
    low = 0
    high = len(list_of_num) - 1
    step = 1

    while low <= high:
        print(f"Step: {step} | Number to Search: {num_to_search} | Low: {low}  | High: {high}  ")
        mid = round(low + high / 2)
        print(f"Mid: {mid}")
        step = step + 1
        if list_of_num[mid] == num_to_search:
            return mid
        elif list_of_num[mid] < num_to_search:
            low = mid + 1
        elif list_of_num[mid] > num_to_search:
            high = mid - 1
        else:
            return None


if __name__ == "__main__":
    print("Main function")
    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = binary_search(numbers, 10)
    if not None :
        print(f"Number found at {result}")
    else:
        print("Not FOund")
