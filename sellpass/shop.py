def get_shops(self):
    r = self.req("get", "/self/shops")
    return self.process_response(r)

def create_shop(self, name: str):
    r = self.req("post", "/self/shops", data = {
        "name": name
    })
    return self.process_response(r)

def edit_shop_name(self, name: str):
    r = self.req("put", f"/self/{self.shop_id}/settings/name", data = {
        "nameName": name
    })
    return self.process_response(r)

def edit_shop_subdomain(self, subdomain: str):
    r = self.req("put", f"/self/{self.shop_id}/settings/subdomain", data = {
        "newSubDomain": subdomain
    })
    return self.process_response(r)

def edit_shop_currency(self, currency: str):
    r = self.req("put", f"/self/{self.shop_id}/settings/currency", data = {
        "currency": currency
    })
    return self.process_response(r)

def edit_shop_timezone(self, utc_timezone_offset: int):
    r = self.req("put", f"/self/{self.shop_id}/settings/timezone", data = {
        "utcTimezoneOffset": utc_timezone_offset
    })
    return self.process_response(r)

def edit_shop_on_hold(self, status: bool):
    r = self.req("put", f"/self/{self.shop_id}/settings/status", data = {
        "onHold": status
    })
    return self.process_response(r)

def edit_shop_popup_message(self, message: str):
    r = self.req("put", f"/self/{self.shop_id}/settings/popup", data = {
        "message": message
    })
    return self.process_response(r)

def edit_shop_terms(self, terms: str):
    r = self.req("put", f"/self/{self.shop_id}/settings/terms", data = {
        "terms": terms
    })
    return self.process_response(r)

def edit_shop_coinbase(self, api_key: str = None, webhook_secret: str = None, gateway_rules: dict = {}):
    r = self.req("put", f"/self/{self.shop_id}/settings/coinbasecommerce", data = {
        "apiKey": api_key,
        "webhookSecret": webhook_secret,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)

def edit_shop_virtual_payments(self, private_key: str = None, public_key: str = None, receive_currency: str = None, gateway_rules: dict = {}):
    r = self.req("put", f"/self/{self.shop_id}/settings/virtual-payments", data = {
        "privateKey": private_key,
        "publicKey": public_key,
        "receiveCurrency": receive_currency,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)

def edit_shop_stripe(self, code: str, gateway_rules: dict):
    r = self.req("put", f"/self/{self.shop_id}/settings/stripeconnect", data = {
        "code": code,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)

def edit_shop_paypal_email(self, email: str, gateway_rules: dict):
    r = self.req("put", f"/self/{self.shop_id}/settings/paypalemail", data = {
        "email": email,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)

def edit_shop_cashapp(self, cashtag, email, gateway_rules: dict):
    r = self.req("put", f"/self/{self.shop_id}/settings/cashapp", data = {
        "cashtag": cashtag,
        "email": email,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)

def edit_shop_paypal_family_and_friends(self, email, gateway_rules: dict):
    r = self.req("put", f"/self/{self.shop_id}/settings/paypal-ff", data = {
        "email": email,
        "gatewayRules": gateway_rules
    })
    return self.process_response(r)