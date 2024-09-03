
def binary_search(list_of_num, num_to_search):
    low = 0
    high = len(list_of_num) - 1
    step = 1

    while low <= high:
        print(f"Step: {step} | Number to Search: {num_to_search} | Low: {low}  | High: {high}  ")
        mid = round(low + high // 2)
        print(f"Mid: {mid}")
        step = step + 1
        if list_of_num[mid] == num_to_search:
            return mid
        elif list_of_num[mid] < num_to_search:
            low = mid + 1
        else:
            high = mid - 1

    print("returning -1")
    return -1


if __name__ == "__main__":
    print("Main function")
    numbers = [1,2,3,4,5,6,7,8,9,10]
    result = binary_search(numbers, 11)
    if result == -1:
        print("Not FOund")
    else:
        print(f"Number found at {result}")
