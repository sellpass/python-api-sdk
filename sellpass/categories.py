def get_categories(self):
    r = self.req("get", f"/self/{self.shop_id}/categories")
    return self.process_response(r)

def create_category(self, name: str, listingids):
    r = self.req("post", f"/self/{self.shop_id}/categories", data = {
        "name": name,
        "listingIds": listingids
    })
    return self.process_response(r)

def get_category(self, category_id: int):
    r = self.req("get", f"/self/{self.shop_id}/categories/{category_id}")
    return self.process_response(r)

def edit_category(self, category_id: int, name: str, listingids):
    r = self.req("put", f"/self/{self.shop_id}/categories/{category_id}", data = {
        "name": name,
        "listingIds": listingids
    })
    return self.process_response(r)

def delete_category(self, category_id: int):
    r = self.req("delete", f"/self/{self.shop_id}/categories/{category_id}")
    return self.process_response(r)