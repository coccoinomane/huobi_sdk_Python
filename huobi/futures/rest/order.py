from huobi.utils.http import post
from huobi.host import HOST_FUTURES
import json


class Order:
    def __init__(self, access_key: str, secret_key: str, host: str = HOST_FUTURES):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__host = host

    def order(self, data: dict = None) -> json:
        path = "/api/v1/contract_order"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def batch_order(self, data: dict = None) -> json:
        path = "/api/v1/contract_batchorder"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cancel(self, data: dict = None) -> json:
        path = "/api/v1/contract_cancel"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def cancel_all(self, data: dict = None) -> json:
        path = "/api/v1/contract_cancelall"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def switch_lever_rate(self, data: dict = None) -> json:
        path = "/api/v1/contract_switch_lever_rate"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_order_info(self, data: dict = None) -> json:
        path = "/api/v1/contract_order_info"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_order_detail(self, data: dict = None) -> json:
        path = "/api/v1/contract_order_detail"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_open_orders(self, data: dict = None) -> json:
        path = "/api/v1/contract_openorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_his_orders(self, data: dict = None) -> json:
        path = "/api/v1/contract_hisorders"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_his_orders_exact(self, data: dict = None) -> json:
        path = "/api/v1/contract_hisorders_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_match_results(self, data: dict = None) -> json:
        path = "/api/v1/contract_matchresults"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def get_match_results_exact(self, data: dict = None) -> json:
        path = "/api/v1/contract_matchresults_exact"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)

    def lightning_close_position(self, data: dict = None) -> json:
        path = "/api/v1/lightning_close_position"
        return post(self.__host, path, self.__access_key, self.__secret_key, data)
