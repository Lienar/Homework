import multiprocessing
from time import sleep
import queue
import random

class WarehouseManager:
    data = {' ' : 0}

    def process_request(self, request):
        if (request[1] == 'receipt'):
            self.receipt(request)

        if (request[1] == 'shipment'):
            self.shipment(request)

    def receipt(self, request):
        if (self.data.get(request[0])):
            self.data[f"{request[0]}_1"] = request[2]
        else:
            self.data[request[0]] = request[2]

    def shipment(self,request):
        if (self.data[request[0]] - request[2] >= 0):
            self.data[request[0]] = self.data[request[0]] - request[2]
        else:
            print (f'Товара недостаточно. Выдано {self.data[request[0]]}')
            self.data[request[0]] = 0


    def run(self, requests):
        for i in range (len(requests)):
         self.process_request(requests[i])
        print(self.data)


manager = WarehouseManager()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        all_requests = [(("product1", "receipt", 100), ("product2", "receipt", 150), ("product1", "shipment", 30),
                         ("product3", "receipt", 200), ("product2", "shipment", 50)),
                        (("product1", "receipt", 90), ("product2", "receipt", 110), ("product1", "shipment", 40),
                         ("product3", "receipt", 100), ("product2", "shipment", 80))]
        pool.map(manager.run, all_requests)
    



























