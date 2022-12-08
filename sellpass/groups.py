def get_groups(self):
    r = self.req("GET", f"/self/{self.shop_id}/groups")
    return self.process_response(r)

def create_group(self, title: str, description: str, product_ids: list, priority: int, type: int, main: bool = True):
    r = self.req("POST", f"/self/{self.shop_id}/groups", data = {
        "title": title,
        "description": description,
        "productIds": product_ids,
        "priority": priority,
        "type": type,
        "main": main
    })
    return self.process_response(r)

def get_group(self, group_id: int):
    r = self.req("GET", f"/self/{self.shop_id}/groups/{group_id}")
    return self.process_response(r)

def edit_group(self, group_id: int, title: str, description: str, product_ids: list, priority: int, type: int, main: bool = True):
    r = self.req("PUT", f"/self/{self.shop_id}/groups/{group_id}", data = {
        "title": title,
        "description": description,
        "productIds": product_ids,
        "priority": priority,
        "type": type,
        "main": main
    })
    return self.process_response(r)

def delete_group(self, group_id: int):
    r = self.req("DELETE", f"/self/{self.shop_id}/groups/{group_id}")
    return self.process_response(r)

def edit_group_thumbnail(self, group_id: int, file: str):
    r = self.req("PUT", f"/self/{self.shop_id}/groups/{group_id}/thumbnail", data = {
        "file": file
    })
    return self.process_response(r)