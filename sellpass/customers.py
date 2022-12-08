def get_customers(self):
    r = self.req("get", f"/self/{self.shop_id}/customers/stats")
    return self.process_response(r)

def get_customer(self, customer_id: int):
    r = self.req("get", f"/self/{self.shop_id}/customers/{customer_id}")
    return self.process_response(r)

def get_customer_ips(self, customer_id: int):
    r = self.req("get", f"/self/{self.shop_id}/customers/{customer_id}/ips")
    return self.process_response(r)