from collections import defaultdict


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    total_pedidos = 0
    dias_semana = ('segunda-feira', 'terça-feira', 'quarta-feira',
                   'quinta-feira', 'sexta-feira', 'sábado', 'domingo')

    cliente_pedidos = []
    prato_favorito = defaultdict(int)

    def __init__(self):
        self.total_pedidos

    def __len__(cls):
        return cls.total_pedidos

    def add_new_order(self, customer, order, day):
        self.total_pedidos += 1
        self.cliente_pedidos.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        conta_pratos = []

        for i in self.cliente_pedidos:
            if i[0] == customer:
                self.prato_favorito[i[1]] += 1

        for i in self.prato_favorito.items():
            conta_pratos.append(i)

        return conta_pratos[1][0]

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    # print(cliente_pedidos)
