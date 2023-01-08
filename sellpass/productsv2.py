def get_productsv2(self):
    r = self.req("get", f"/self/{self.shop_id}/v2/products")
    return self.process_response(r)

def create_productv2(self, title: str, description: str, variants: list, path: str, seo: str, unlisted: bool = False, private: bool = False, on_hold: bool = False, short_description: str = None):
    r = self.req("post", f"/self/{self.shop_id}/v2/products", data = {
        "title": title,
        "description": description,
        "variants": variants,
        "path": path,
        "seo": seo,
        "unlisted": unlisted,
        "private": private,
        "on_hold": on_hold,
        "shortDescription": short_description
    })
    return self.process_response(r)

def edit_productv2_thumbnail(self, product_id: int, file: str):
    r = self.req("put", f"/self/{self.shop_id}/v2/products/{product_id}/thumbnail", data = {
        "file": file
    })
    return self.process_response(r)

def edit_productv2_seo_image(self, product_id: int, file: str):
    r = self.req("put", f"/self/{self.shop_id}/v2/products/{product_id}/seo/image", data = {
        "file": file
    })
    return self.process_response(r)

def get_productv2(self, product_id: int):
    r = self.req("get", f"/self/{self.shop_id}/v2/products/{product_id}")
    return self.process_response(r)

def edit_productv2(self, product_id: int, title: str, description: str, variants: list, path: str, seo: str, unlisted: bool = False, private: bool = False, on_hold: bool = False, short_description: str = None):
    r = self.req("put", f"/self/{self.shop_id}/v2/products/{product_id}", data = {
        "title": title,
        "description": description,
        "variants": variants,
        "path": path,
        "seo": seo,
        "unlisted": unlisted,
        "private": private,
        "on_hold": on_hold,
        "shortDescription": short_description
    })
    return self.process_response(r)

def bulk_edit_productsv2_payment_method(self, product_ids: list, gateways_list: dict):
    r = self.req("put", f"/self/{self.shop_id}/v2/products/payment-method", data = {
        "productIds": product_ids,
        "gatewaysList": gateways_list
    })
    return self.process_response(r)
