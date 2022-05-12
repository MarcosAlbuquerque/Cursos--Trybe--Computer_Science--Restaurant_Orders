from collections import defaultdict
import csv

order_counter = defaultdict(int)
file_mkt = 'data/mkt_campaign.txt'
arnaldo = []
maria = []
joao = set()
joao_days = set()
days_jobs = set()


def analyze_log(path_to_file):
    verify_file(path_to_file)
    read_file(path_to_file)
    write_file(file_mkt)


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
        counted_order()


def separate_order(order):
    for i in order:
        order_counter[i["cliente"], i["pedido"]] += 1
        days_jobs.add(i['dia'])

        if i['cliente'] == 'joao':
            joao_days.add(i['dia'])


def counted_order():
    for i in order_counter.items():
        append_maria(i)
        append_arnaldo(i)

        if i[0][0] == 'joao':
            for j, v in order_counter.items():
                if j[1] != i[0][1]:
                    joao.add(j[1])


def append_maria(i):
    if i[0][0] == 'maria':
        maria.append((i[1], i[0][1]))


def append_arnaldo(i):
    if i[0][0] == 'arnaldo':
            arnaldo.append((i[1], i[0][1]))

def write_file(file_mkt):
    with open(file_mkt, 'a') as file:
        file.write(f"{max(maria)[1]}\n")
        file.write(f"{arnaldo[1][0]}\n")
        file.write(f"{joao}\n")
        file.write(f"{days_jobs.difference(joao_days)}")
        file.close()
