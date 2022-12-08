def get_public_shop(self):
    r = self.req("get", "/self/shops")
    return self.process_response(r)

def get_public_shop_info(self):
    r = self.req("get", f"/v2/public/shops/{self.shop_id}/main")
    return self.process_response(r)

def get_public_shop_listings(self):
    r = self.req("get", f"/v2/public/shops/{self.shop_id}/listings")
    return self.process_response(r)

def get_public_shop_feedback(self):
    r = self.req("get", f"/v2/public/shops/{self.shop_id}/feedbacks")
    return self.process_response(r)

def get_public_shop_announcements(self):
    r = self.req("get", f"/v2/public/shops/{self.shop_id}/main")
    return self.process_response(r)

def get_public_shop_faqs(self):
    r = self.req("get", f"/v2/public/shops/{self.shop_id}/faqs")
    return self.process_response(r)