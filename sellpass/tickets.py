def get_tickets(self):
    r = self.req("get", f"/self/{self.shop_id}/tickets")
    return self.process_response(r)

def get_ticket(self, ticket_id: int):
    r = self.req("get", f"/self/{self.shop_id}/tickets/{ticket_id}")
    return self.process_response(r)

def close_ticket(self, ticket_id: int):
    r = self.req("put", f"/self/{self.shop_id}/tickets/{ticket_id}/close")
    return self.process_response(r)

def answer_ticket(self, message: str, ticket_id: int):
    r = self.req("post", f"/self/{self.shop_id}/tickets/{ticket_id}/answer", data = {
        "content": message
    })
    return self.process_response(r)

