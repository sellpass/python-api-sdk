def get_products(self):
    r = self.req("GET", f"/self/{self.shop_id}/products")
    return self.process_response(r)

def delete_product(self, product_id: int):
    r = self.req("DELETE", f"/self/{self.shop_id}/products/{product_id}")
    return self.process_response(r)

def bulk_edit_product_fields(self, product_ids: list = [], custom_fields: list = []):
    r = self.req("PUT", f"/self/{self.shop_id}/products/bulk/update/custom-fields", data = {
        "productIds": product_ids,
        "customFields": custom_fields
    })
    return self.process_response(r)

def bulk_edit_product_notes(self, note: str, product_ids: list = []):
    r = self.req("PUT", f"/self/{self.shop_id}/products/bulk/update/customer-note", data = {
        "productIds": product_ids,
        "note": note
    })
    return self.process_response(r)

def bulk_edit_product_visibility(self, product_ids: list = [], unlisted: bool = False, private: bool = False, on_hold: bool = False):
    r = self.req("PUT", f"/self/{self.shop_id}/products/bulk/update/visibility", data = {
        "productIds": product_ids,
        "unlisted": unlisted,
        "private": private,
        "onHold": on_hold
    })
    return self.process_response(r)

def bulk_edit_product_discord_integration(self, discord_social_connect_settings: dict, product_ids: list = []):
    r = self.req("PUT", f"/self/{self.shop_id}/products/bulk/update/visibility", data = {
        "productIds": product_ids,
        "discordSocialConnectSettings": discord_social_connect_settings
    })
    return self.process_response(r)

def bulk_delete_products(self, product_ids: list = []):
    r = self.req("POST", f"/self/{self.shop_id}/products/bulk/delete", data = {
        "productIds": product_ids
    })
    return self.process_response(r)