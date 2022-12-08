def get_invoices(self):
    r = self.req("GET", f"/self/{self.shop_id}/orders")
    return self.process_response(r)

def get_invoice(self, invoice_id: str):
    r = self.req("GET", f"/self/{self.shop_id}/orders/{invoice_id}")
    return self.process_response(r)

def resend_invoice_email(self, invoice_id: str):
    r = self.req("POST", f"/self/{self.shop_id}/orders/{invoice_id}/resend")
    return self.process_response(r)

def replace_invoice(self, invoice_id: str, part_invoice_id: int, quantity: int = 1):
    r = self.req("POST", f"/self/{self.shop_id}/orders/{invoice_id}/replace", data = {
        "partInvoiceId": part_invoice_id,
        "quantity": quantity
    })
    return self.process_response(r)

def process_invoice(self, invoice_id: str):
    r = self.req("POST", f"/self/{self.shop_id}/orders/{invoice_id}/process")
    return self.process_response(r)

