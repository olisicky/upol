import csv

def filter_students(f_name, limit=20):

    try:
        f = open(f_name, "r", 1, "latin-1")    #'./ukol.csv'
        reader = csv.DictReader(f, delimiter=';')
        res = [dict(s) for s in reader]
    except:
        print('Chyba při práci se souborem.')
    finally:
        f.close()

    filtered = []
    for stud in res:
        if int(stud['kredity']) > limit:
            filtered.append(stud)
    return filtered


def write_result(students):

    hlavicka = students[0].keys()
    try:
        f = open('./ukol-20.csv', "w", 1, "latin-1", newline='')
        print('heere')
        writer = csv.DictWriter(f, fieldnames=hlavicka, delimiter=';')
        writer.writeheader()
        writer.writerows(students)
    except:
        print('Chyba při práci se souborem.')
    finally:
        f.close()
        return True
    
if __name__ == '__main__':

    filtered = filter_students('./ukol.csv')
    write_result(filtered)
