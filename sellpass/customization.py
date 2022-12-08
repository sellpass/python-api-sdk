def get_design(self):
    r = self.req("get", f"/self/{self.shop_id}/customization")
    return self.process_response(r)

def edit_design(
    self,
    primary_color: str,
    background_color: str,
    secondary_color: str,
    primary_text_color: str,
    secondary_text_color: str,
    dark_mode: bool,
    disable_business_name: bool,
    disable_search_bar: bool,
    disable_product_title: bool,
    disable_business_logo: bool,
    disable_reviews: bool,
    disable_products_sold: bool,
    hide_out_of_stock_products: bool,
    disable_shadows: bool = False,
    disable_support: bool = False,
    primary_color_accent: str = None,
    font_link: str = None
    ):
    r = self.req("put", f"/self/{self.shop_id}/customization/design", data = {
        "primaryColor": primary_color,
        "primaryColorAccent": primary_color_accent,
        "backgroundColor": background_color,
        "secondaryColor": secondary_color,
        "primaryTextColor": primary_text_color,
        "secondaryTextColor": secondary_text_color,
        "darkMode": dark_mode,
        "disableBusinessName": disable_business_name,
        "disableSearchBar": disable_search_bar,
        "disableProductTitle": disable_product_title,
        "disableBusinessLogo": disable_business_logo,
        "disableReviews": disable_reviews,
        "disableProductsSold": disable_products_sold,
        "hideOutOfStockProducts": hide_out_of_stock_products,
        "disableShadows": disable_shadows,
        "disableSupport": disable_support,
        "fontLink": font_link
    })
    return self.process_response(r)

def edit_widgets(self, crisp_key: str = None, google_analytics_key: str = None, hotjar_key: str = None, intercom_key: str = None):
    r = self.req("put", f"/self/{self.shop_id}/customization/widgets", data = {
        "crispKey": crisp_key,
        "googleAnalyticsKey": google_analytics_key,
        "hotjarKey": hotjar_key,
        "intercomKey": intercom_key
    })
    return self.process_response(r)

def edit_storefront(self, title: str = None, description: str = None, button_text: str = None, disable_button: bool = False, disable_title: bool = False, disable_description: bool = False):
    r = self.req("put", f"/self/{self.shop_id}/customization/storefront", data = {
        "title": title,
        "description": description,
        "buttonText": button_text,
        "disableButton": disable_button,
        "disableTitle": disable_title,
        "disableDescription": disable_description
    })
    return self.process_response(r)

def edit_background(self, file: str):
    r = self.req("post", f"/self/{self.shop_id}/customization/background", data = {
        "file": file
    })
    return self.process_response(r)
    
def edit_seo(self, title: str, description: str):
    r = self.req("put", f"/self/{self.shop_id}/customization/seo", data = {
        "metaTitle": title,
        "metaDescription": description
    })
    return self.process_response(r)

def edit_seo_image(self, file: str):
    r = self.req("post", f"/self/{self.shop_id}/customization/seo/image", data = {
        "file": file
    })
    return self.process_response(r)

def edit_seo_favicon(self, file: str):
    r = self.req("post", f"/self/{self.shop_id}/customization/seo/favicon", data = {
        "file": file
    })
    return self.process_response(r)

def edit_logo(self, file: str):
    r = self.req("post", f"/self/{self.shop_id}/customization/logo", data = {
        "file": file
    })
    return self.process_response(r)

def edit_links(self, social_links: list):
    r = self.req("put", f"/self/{self.shop_id}/customization/links", data = {
        social_links
    })
    return self.process_response(r)

