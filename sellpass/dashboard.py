def get_dashboard(self):
    r = self.req("GET", f"/self/{self.shop_id}/dashboard/general")
    return self.process_response(r)