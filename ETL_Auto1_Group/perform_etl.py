import csv
import json

words_to_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                    '-': -1
                    }


def load(data_file_name):
    row_record = []
    with open('ETL_Auto1_Group/data/' + data_file_name, 'r') as datafile:
        file = csv.DictReader(datafile, delimiter=';')
        for line in file:
            row_record.append(dict(line))
        return row_record[1:]


def bad_records_filter(row):
    if (
        (row['engine-location'].strip() == '-') or
        (row['num-of-cylinders'].strip() == '-') or
        (row['engine-size'].strip() == '-') or
        (row['weight'].strip() == '-') or
        (row['horsepower'].strip() == '-') or
        (row['aspiration'].strip() == '-') or
        (row['price'].strip() == '-') or
            (row['make'].strip() == '-')):
        return True
    else:
        return False


def write_to_csv(record_set, delimiter, output_filename):
    with open('ETL_Auto1_Group/'+output_filename, 'w+') as target:
        csv_writer = csv.writer(target, delimiter=delimiter)
        csv_writer.writerows(record_set)


def transform(file_name):
    rows = load(file_name)
    final_records = []
    error_records = []
    for observation in rows:
        if bad_records_filter(observation) == True:
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
    header = list(final_records[0].keys())
    records = [list(row.values()) for row in final_records]
    records.insert(0, header)
    # print(records)
    # print('{} + {} = {}'.format(len(final_records), len(error_records), len(rows)))
    write_to_csv(records, ',', 'output.csv')
    print("Output file generated!")
    return records


if __name__ == "__main__":
    x = transform('Challenge_me.txt')
    print(x)