from collections import defaultdict
import csv

arnaldo = []
maria = []
joao = set()
joao_days = set()
days_jobs = set()
order_counter = defaultdict(int)


def analyze_log(path_to_file):
    verify_file(path_to_file)
    read_file(path_to_file)
    write_file()


def verify_file(path_to_file):
    errorExtension = path_to_file[len(path_to_file) - 12:]

    if errorExtension[-3:] != 'csv':
        raise FileNotFoundError(f"Extensão inválida: \'{path_to_file}\'")
    if errorExtension != 'orders_1.csv':
        raise FileNotFoundError(f"Arquivo inexistente: \'{path_to_file}\'")


def read_file(path_to_file):
    with open(path_to_file) as file:
        fieldnames = ['cliente', 'pedido', 'dia']
        order = csv.DictReader(file, fieldnames)

        separate_order(order)

        for i in order_counter.items():
            if i[0][0] == 'maria':
                maria.append((i[1], i[0][1]))

            if i[0][0] == 'arnaldo':
                arnaldo.append((i[1], i[0][1]))

            if i[0][0] == 'joao':
                for j, v in order_counter.items():
                    if j[1] != i[0][1]:
                        joao.add(j[1])


def separate_order(order):
    for i in order:
        order_counter[i["cliente"], i["pedido"]] += 1
        days_jobs.add(i['dia'])

        if i['cliente'] == 'joao':
            joao_days.add(i['dia'])


def write_file():
    with open('data/mkt_campaign.txt', 'a') as file:
        file.write(f"{max(maria)[1]}\n")
        file.write(f"{arnaldo[1][0]}\n")
        file.write(f"{joao}\n")
        file.write(f"{days_jobs.difference(joao_days)}")
        file.close()
