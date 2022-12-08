def get_feedback(self):
    r = self.req("GET", f"/self/{self.shop_id}/feedbacks")
    return self.process_response(r)

def get_feedback_appeals(self):
    r = self.req("GET", f"/self/{self.shop_id}/feedbacks/appeals")
    return self.process_response(r)

def get_feedback_item(self, feedback_id: int):
    r = self.req("GET", f"/self/{self.shop_id}/feedbacks/{feedback_id}")
    return self.process_response(r)

def answer_feedback_item(self, feedback_id: int, answer: str):
    r = self.req("POST", f"/self/{self.shop_id}/feedbacks/{feedback_id}/answer", data = {
        "answer": answer
    })
    return self.process_response(r)

def appeal_feedback_item(self, feedback_id: int, reason: int, description: str):
    r = self.req("POST", f"/self/{self.shop_id}/feedbacks/{feedback_id}/appeal", data = {
        "reason": reason,
        "description": description
    })
    return self.process_response(r)