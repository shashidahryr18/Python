file1 = open("C:/Users/Shashidhar/Downloads/ict.txt")

file1 = open(r"C:/Users/Shashidhar/Downloads/ict.txt")

# This will print every line one by one in the file
for i in file1:
    print(i)

file1 = open(r"C:/Users/Shashidhar/Downloads/ict.txt")
print(file1.read())

with open(r"C:/Users/Shashidhar/Downloads/ict.txt", 'r') as f1:
    data = f1.read()
print(data)

f1 = open(r"C:/Users/Shashidhar/Downloads/ict.txt")
print(f1.read(5))

with open(r"C:/Users/Shashidhar/Downloads/ict.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

print(word)

file = open("3EK2A.txt", 'w')
file.write("ICT ICT ICT \n")
file.write("ICT ICT ICT ICT ICT")
file.close()

with open("Marwadi_university.txt", "w") as f:
    f.write("Hello kitty!!!")

file = open("3EK2A.txt", 'a')
file.write("\n Department Department")
file.close()

with open(r'C:/Users/Shashidhar/Downloads/a.tif', 'rb') as file:
    binary_data = file.read()

with open(r'C:/Users/Shashidhar/Downloads/a.tif', 'wb') as f:
    f.write(binary_data)

import csv

# Reading from a CSV file
with open(r'C:/Users/Shashidhar/Downloads/data-1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])

# Post Lab

def count_file_contents(filename):
    lines = 0
    words = 0
    characters = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {characters}")

if __name__ == "__main__":
    filepath = r"C:/Users/Shashidhar/Downloads/ict.txt"
    count_file_contents(filepath)

def read_file_to_list(filename):
    lines_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines_list.append(line.rstrip('\n'))
    return lines_list

if __name__ == "__main__":
    filepath = r"C:/Users/Shashidhar/Downloads/ict.txt"
    lines = read_file_to_list(filepath)
    print(lines)

import csv

def read_csv_and_print(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

if __name__ == "__main__":
    filepath = r"C:/Users/Shashidhar/Downloads/data-1.csv"
    read_csv_and_print(filepath)

def merge_files(file1, file2, merged_file):
    with open(merged_file, 'w', encoding='utf-8') as outfile:
        with open(file1, 'r', encoding='utf-8') as f1:
            for line in f1:
                outfile.write(line)

        with open(file2, 'r', encoding='utf-8') as f2:
            for line in f2:
                outfile.write(line)

if __name__ == "__main__":
    file1_path = r"C:/Users/Shashidhar/Downloads/ict.txt"
    file2_path = r"C:/Users/Shashidhar/Downloads/ict.txt"
    merged_file_path = r"C:/Users/Shashidhar/Downloads/merged.txt"

    merge_files(file1_path, file2_path, merged_file_path)
    print(f"Files merged into {merged_file_path}")
