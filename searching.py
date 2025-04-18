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

    allowed_fields = {"unordered_numbers","ordered_numbers","dna_sequence"}

    if field not in allowed_fields:
        return None

    with open(file_path,"r") as json_file:
        sequential = json.load(json_file)

    return sequential[field]

def linear_search(sequence,wanted_number):

    new_dict = {}
    index_numbers = []

    for i in range(len(sequence)):
        if sequence[i] == wanted_number:
            index_numbers.append(i)

    new_dict['positions'] = index_numbers
    new_dict["count"] = sequence.count(wanted_number)

    return new_dict

def pattern_search(sequence,wanted_value):

    value_list = []
    sequence_list = list(sequence)
    sequence_str = ""

    for i in sequence_list:
        if isinstance(i,str):
            sequence_str += i

    for i in range(len(sequence_str)):
        if sequence_str[i:i+3] == wanted_value:
            value_list.append(wanted_value)

    mnozina = value_list.count(wanted_value)

    return mnozina

def main():
    numbers = read_data('sequential.json','dna_sequence')
    print(numbers)
    #wanted_number = linear_search(numbers,5)
    #print(wanted_number)
    wanted_value = pattern_search(numbers,"ATA")
    print(wanted_value)


if __name__ == '__main__':
    main()