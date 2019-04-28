import csv
import json

words_to_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                    '-': -1
                    }


def load(data_file_name):
    row_record = []
    with open('data/'+data_file_name, 'r') as datafile:
        file = csv.DictReader(datafile, delimiter=';')
        for line in file:
            row_record.append(dict(line))
        return row_record[1:]


def transform(rows):
    # print(rows)
    final_records = []
    error_records = []
    for observation in rows:
        if (
            (observation['engine-location'].strip() == '-') or
            (observation['num-of-cylinders'].strip() == '-') or
            (observation['engine-size'].strip() == '-') or
            (observation['weight'].strip() == '-') or
            (observation['horsepower'].strip() == '-') or
            (observation['aspiration'].strip() == '-') or
            (observation['price'].strip() == '-') or
            (observation['make'].strip() == '-')
        ):
            error_records.append(rows)
            continue
        row_dict = {}
        # Logic for 'engine-location'
        row_dict['engine-location'] = observation['engine-location']
        # Logic for 'num-of-cylinders'
        row_dict['num-of-cylinders'] = words_to_numbers[observation['num-of-cylinders'].strip()]
        # Logic for engine-size
        row_dict['engine-size'] = int(observation['engine-size'])
        # Logic for weight
        row_dict['weight'] = int(observation['weight'])
        # Logic for horsepower
        row_dict['horsepower'] = float(
            observation['horsepower'].replace(',', '.'))
        # Logic for aspiration
        row_dict['aspiration'] = 1 if observation['aspiration'] == 'turbo' else 0
        # Logic for price
        row_dict['price'] = int(observation['price'])/100.0
        # Logic for make
        row_dict['make'] = observation['make']
        final_records.append(row_dict)
    return (final_records, error_records)


def main():
    rows = load('Challenge_me.txt')
    output_records, bad_records = transform(rows)
    # print('{} + {} = {}'.format(len(output_records), len(bad_records), len(rows)))
    header = list(output_records[0].keys())
    records = [list(row.values()) for row in output_records]
    records.insert(0, header)
    print(records)


if __name__ == "__main__":
    main()
