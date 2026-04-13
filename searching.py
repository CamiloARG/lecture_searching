from pathlib import Path
import json

def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    allowed_fields = {"unordered_numbers","ordered_numbers", "dna_sequence"}

    if field not in allowed_fields:
        return None

    with open(file_path,"r") as json_file:
        sequential_data = json.load(json_file)

    return sequential_data[field]

def linear_search(sequence,number):
    new_dict = {}
    index_numbers = []

    for i in range(len(sequence)):
        if sequence[i] == number:
            index_numbers.append(i)

    new_dict['positions'] = index_numbers
    new_dict["count"] = sequence.count(number)

    return new_dict

def binarny_search(numbers_list,number):
    if number not in numbers_list:
        return None
    left_num_margin_idx = 0
    half_num_idx = (len(numbers_list) // 2) - 1
    right_num_margin_idx = -1

    while True:
        if numbers_list[half_num_idx] == number:
            return half_num_idx

        if numbers_list[left_num_margin_idx] == number:
            return left_num_margin_idx

        if numbers_list[right_num_margin_idx] == number:
            return len(numbers_list)-1

        if numbers_list[half_num_idx] < number:
            left_margin_idx = half_num_idx+1
            half_idx = (len(numbers_list[half_num_idx:])//2) + half_num_idx - 1
            right_margin_idx = -1
            if numbers_list[left_margin_idx] == number:
                return left_margin_idx
            if numbers_list[half_idx] == number:
                return half_idx
            if numbers_list[right_margin_idx] == number:
                return len(numbers_list)-1
            else:
                for i in range(len(numbers_list[left_margin_idx:right_margin_idx])+half_num_idx):
                    if numbers_list[i] == number:
                        return i
        if numbers_list[half_num_idx] > number:
            left_right_margin_idx = half_num_idx-1
            left_half_left_li = (len(numbers_list[:half_num_idx])//2) - 1
            left_left_margin_idx = 0

            if numbers_list[left_right_margin_idx] == number:
                return left_right_margin_idx
            if numbers_list[left_half_left_li] == number:
                return left_half_left_li
            if numbers_list[left_left_margin_idx] == number:
                return left_left_margin_idx
            else:
                for i in range(len(numbers_list[:half_num_idx])):
                    if numbers_list[i] == number:
                        return i

def main():
    numbers = read_data('sequential.json', 'ordered_numbers')
    print(numbers)
    # wanted_number = linear_search(numbers,5)
    # print(wanted_number)
    wanted_idx = binarny_search(numbers,70)
    print(wanted_idx)

if __name__ == "__main__":
    main()
