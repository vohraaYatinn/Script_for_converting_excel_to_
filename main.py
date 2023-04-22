
import csv

list_number = []
dict_names_phone = {}
# opening the CSV file
with open('customer.csv', mode='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        if lines:
            if lines[1] not in list_number:
                if lines[1][0] == "0":
                    lines[1] = lines[1][1:]
                if lines[1].isdigit():
                    if len(lines[1]) == 10:
                        dict_names_phone[lines[0]] = lines[1]
                        list_number.append(lines[1])


file = open('contacts_updated.vcf', 'w')

for i in dict_names_phone:
    if counter == 10:
        break
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:2.1\n")
    file.write(f"N:;{i};;;\n")
    file.write(f"FN:{i}\n")
    file.write(f"TEL;CELL:{dict_names_phone[i]}\n")
    file.write("END:VCARD\n")
    counter = counter + 1

file.close()
