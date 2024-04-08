import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open("sequential.json", mode="r") as data_file:
        data = json.load(data_file)

    if field in data.keys():
        return data[field]
    else:
        return None

def linear_search(sequence, number):
    """
    Search the sequence and the number, where it is located
    :param sequence:searched sequence
    :param number:found number
    :return:dictionary with two keys, first key the position and the second one the number of ocurrences
    """
    positions = []

    for i, cislo in enumerate(sequence):
        if cislo == number:
            positions.append(i)
        else:
            pass

    return {"positions": positions, "count": len(positions)}

def pattern_search(searched_sequence,searched_pattern):
    """

    :param searched_sequence:
    :param searched_pattern:
    :return:
    """
    with open("sequential.json", mode="r") as data_file:
        data = json.load(data_file)
        searched_sequence = data["dna_sequence"]

    list_idx = []

    for i, number in enumerate(searched_sequence):
        if number in enumerate(searched_pattern):
            list_idx.append(i)
        else:
            pass

    return list_idx


def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    searched_number = linear_search("sequential.json", 31)
    searched_pattern = pattern_search("ATA", 1)
    print(sequential_data)
    print(searched_number)
    print(searched_pattern)
if __name__ == '__main__':
    main()