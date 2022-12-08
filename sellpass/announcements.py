def get_announcements(self):
    r = self.req("get", f"/self/{self.shop_id}/announcements")
    return self.process_response(r)

def create_announcement(self, title: str, short_description: str, description: str, unlisted: bool, private: bool, button_text: str = None, button_link: str = None):
    r = self.req("post", f"/self/{self.shop_id}/announcements", data = {
        "title": title,
        "shortDescription": short_description,
        "description": description,
        "unlisted": unlisted,
        "private": private,
        "buttonText": button_text,
        "buttonLink": button_link
    })
    return self.process_response(r)

def edit_announcement(self, announcement_id: str, title: str, short_description: str, description: str, unlisted: bool, private: bool, button_text: str = None, button_link: str = None):
    r = self.req("put", f"/self/{self.shop_id}/announcements/{announcement_id}", data = {
        "title": title,
        "shortDescription": short_description,
        "description": description,
        "unlisted": unlisted,
        "private": private,
        "buttonText": button_text,
        "buttonLink": button_link
    })
    return self.process_response(r)

def delete_announcement(self, announcement_id: str):
    r = self.req("delete", f"/self/{self.shop_id}/announcements/{announcement_id}")
    return self.process_response(r)