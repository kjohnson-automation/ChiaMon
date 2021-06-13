import requests

class Netspace():
    """ Creates netspace class object for updated Chia network info
    """
    def __init__(self):
        """ Sets base requests url
        """
        self.base_url = "https://api.chiaprofitability.com/{request}"

    def get_request(self, request_str:str):
        """ handles the get/rsp check
        Returns: json dictionary
        """
        url = self.base_url.format(request=request_str)
        rsp = requests.get(f"{url}")
        if rsp.status_code == 200:
            return rsp.json()
        else:
            return -1

    def get_netspace(self):
        """ Gets Chia network netspace information
        """
        rsp = self.get_request("netspace")
        if rsp != -1:
            self.netspace = rsp["netspace"]
            self.daychange = rsp["daychange"]

    def get_market_data(self):
        """ Returns the Chia market data """
        rsp = self.get_request("market")
        if rsp != -1:
            self.price = rsp["price"]
            self.day_min = rsp["daymin"]
            self.day_max = rsp["daymax"]
            self.day_change = rsp["daychange"]
