def get_listings(self):
    r = self.req("GET", f"/self/{self.shop_id}/listings")
    return self.process_response(r)

def edit_listings_position(self, listings: list):
    r = self.req("PUT", f"/self/{self.shop_id}/listings/position", data = {
        "listings": listings
    })
    return self.process_response(r)