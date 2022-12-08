def get_coupons(self):
    r = self.req("get", f"/self/{self.shop_id}/coupons")
    return self.process_response(r)

def create_coupon(
    self,
    name: str,
    discount: float,
    is_fixed: bool,
    note: str = None,
    start_date: str = None,
    end_date: str = None,
    restrct_to_products: list = None,
    restrict_to_gateways: list = None,
    max_uses: int = None
    ):
    r = self.req("post", f"/self/{self.shop_id}/coupons", data = {
        "name": name,
        "note": note,
        "discount": discount,
        "isFixed": is_fixed,
        "startDate": start_date,
        "endDate": end_date,
        "restrictToProducts": restrct_to_products,
        "restrictToGateways": restrict_to_gateways,
        "maxUses": max_uses
    })
    return self.process_response(r)

def get_coupon(self, coupon_id: int):
    r = self.req("get", f"/self/{self.shop_id}/coupons/{coupon_id}")
    return self.process_response(r)

def edit_coupon(self,
    coupon_id: int,
    name: str,
    discount: float,
    is_fixed: bool,
    note: str = None,
    start_date: str = None,
    end_date: str = None,
    restrct_to_products: list = None,
    restrict_to_gateways: list = None,
    max_uses: int = None
    ):
    r = self.req("put", f"/self/{self.shop_id}/coupons/{coupon_id}", data = {
        "name": name,
        "note": note,
        "discount": discount,
        "isFixed": is_fixed,
        "startDate": start_date,
        "endDate": end_date,
        "restrictToProducts": restrct_to_products,
        "restrictToGateways": restrict_to_gateways,
        "maxUses": max_uses
    })
    return self.process_response(r)

def delete_coupon(self, coupon_id: int):
    r = self.req("delete", f"/self/{self.shop_id}/coupons/{coupon_id}")
    return self.process_response(r)