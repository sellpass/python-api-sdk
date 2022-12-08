def get_faqs(self):
    r = self.req("GET", f"/self/{self.shop_id}/faqs")
    return self.process_response(r)

def create_faq(self, question: str, answer: str):
    r = self.req("POST", f"/self/{self.shop_id}/faqs", data = {
        "question": question,
        "answer": answer,
    })
    return self.process_response(r)

def edit_faq(self, faq_id: int, question: str, answer: str):
    r = self.req("PUT", f"/self/{self.shop_id}/faqs/{faq_id}", data = {
        "question": question,
        "answer": answer,
    })
    return self.process_response(r)

def delete_faq(self, faq_id: int):
    r = self.req("DELETE", f"/self/{self.shop_id}/faqs/{faq_id}")
    return self.process_response(r)