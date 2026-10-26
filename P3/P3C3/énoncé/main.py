from pathlib import Path
import csv

def extract(file_name):
    file = Path(__file__).parent / file_name

    with open(file, 'r') as file_csv:
        reader = csv.DictReader(file_csv, delimiter=',')
        return list(reader)


def main():
    header = ['nom', 'salaire']
    file_name = Path(__file__).parent / 'output.csv'

    with open(file_name, 'w') as file_csv:
        writer = csv.writer(file_csv, delimiter=',')
        writer.writerow(header)

        for person in extract('input.csv'):
            line = [person.get('nom'), int(person.get('heures_travaillees')) * 15]
            
            writer.writerow(line)

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
