
import csv
def tsql(x):
    with open(x + ".CSV") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                a = f"INSERT INTO {x} \n({','.join(row)})"
                f = open(x + ".txt", "w+")
                f.write(a)
                f.close()
                #print(a)
                line_count += 1
                f = open(x + ".txt", "a+")
                f.write(f'\nVALUES\n')
                f.close()

            else:
                f = open(x + ".txt", "a+")
                l = "','"
                b = f"('{l.join(row)}',),"
                f.write(b + '\n')
                f.close()
                    #print(f' \t {row[0]} , {row[1]} , {row[2]}, .')
                line_count += 1
        print(f'Processed {line_count} lines.')


tsql('PROJECTS')

