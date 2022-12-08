def get_blacklist(self):
    r = self.req("get", f"/self/{self.shop_id}/blacklist")
    return self.process_response(r)

def create_blocked_item(self, data: str, note: str, type: int):
    r = self.req("post", f"/self/{self.shop_id}/blacklist", data = {
        "data": data,
        "note": note,
        "type": type,
        "customerForShopId": self.shop_id
    })
    return self.process_response(r)

def get_blocked_item(self, blocked_id: int):
    r = self.req("get", f"/self/{self.shop_id}/blacklist/{blocked_id}")
    return self.process_response(r)

def edit_blocked_item(self, blocked_id: int, data: str, note: str, type: int):
    r = self.req("put", f"/self/{self.shop_id}/blacklist/{blocked_id}", data = {
        "data": data,
        "note": note,
        "type": type,
        "customerForShopId": self.shop_id
    })
    return self.process_response(r)

def delete_blocked_item(self, blocked_id: int):
    r = self.req("delete", f"/self/{self.shop_id}/blacklist/{blocked_id}")
    return self.process_response(r)