from collections import defaultdict


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    total_pedidos = 0
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
        todos_pratos = set()
        prato_pedido = set()

        for i in self.cliente_pedidos:
            if i[1] not in 'frango':
                todos_pratos.add(i[1])

            if i[0] == customer:
                prato_pedido.add(i[1])

        prato_nao_pedido = todos_pratos.difference(prato_pedido)
        return(prato_nao_pedido)

    def get_days_never_visited_per_customer(self, customer):
        dias_visitados = set()
        dias_da_semana = set()

        for i in self.cliente_pedidos:
            if i[2] not in 'domingo':
                dias_da_semana.add(i[2])

            if i[0] == customer:
                dias_visitados.add(i[2])

        dias_nao_visitados = dias_da_semana.difference(dias_visitados)
        return dias_nao_visitados

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    # print(cliente_pedidos)
