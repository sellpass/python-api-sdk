import httpx

class SellPass:
    from .public import get_public_shop, get_public_shop_info, get_public_shop_listings, get_public_shop_feedback, get_public_shop_announcements
    from .announcements import get_announcements, create_announcement, edit_announcement, delete_announcement
    from .blacklist import get_blacklist, create_blocked_item, get_blocked_item, edit_blocked_item, delete_blocked_item
    from .categories import get_categories, create_category, get_category, edit_category, delete_category
    from .coupons import get_coupons, create_coupon, get_coupon, edit_coupon, delete_coupon
    from .customization import get_design, edit_design, edit_widgets, edit_storefront, edit_background, edit_seo, edit_seo_image, edit_seo_favicon, edit_logo, edit_links
    from .dashboard import get_dashboard
    from .faqs import get_faqs, create_faq, edit_faq, delete_faq
    from .feedback import get_feedback, get_feedback_item, answer_feedback_item, appeal_feedback_item, get_feedback_appeals
    from .groups import get_groups, create_group, get_group, edit_group, delete_group, edit_group_thumbnail
    from .orders import get_invoices, get_invoice, resend_invoice_email, replace_invoice, process_invoice
    from .listings import get_listings, edit_listings_position
    from .products import get_products, delete_product, bulk_delete_products, bulk_edit_product_discord_integration, bulk_edit_product_fields, bulk_edit_product_notes, bulk_edit_product_visibility
    from .shop import get_shops, create_shop, edit_shop_cashapp, edit_shop_coinbase, edit_shop_currency, edit_shop_name, edit_shop_on_hold, edit_shop_paypal_email, edit_shop_paypal_family_and_friends, edit_shop_popup_message, edit_shop_stripe, edit_shop_subdomain, edit_shop_terms, edit_shop_timezone, edit_shop_virtual_payments
    from .tickets import get_tickets, get_ticket, close_ticket, answer_ticket
    from .productsv2 import get_productsv2, create_productv2, edit_productv2, get_productv2, bulk_edit_productsv2_payment_method, edit_productv2_thumbnail, edit_productv2_seo_image
    from .customers import get_customers, get_customer, get_customer_ips
    
    def __init__(self, api_key: str, debug: bool = False, shop_id: str = None):
        self.api_key = api_key
        self.debug = debug
        self.base_url = "https://dev.sellpass.io"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        if not shop_id:
            self.shop_id = self.get_public_shop()[0]["shop"]["id"]
        else:
            self.shop_id = shop_id

    def debug_print(self, message: str):
        if self.debug:
            print(message)
        
    def req(self, method: str, path: str = "", data: dict = None):
        url = f"{self.base_url}{path}"
        
        method = method.lower()
        self.debug_print(f"{method} request to: {url}")
        
        if method == "get":
            r = httpx.get(url, headers=self.headers)
        elif method == "post":
            r = httpx.post(url, headers=self.headers, json=data)
        elif method == "put":
            r = httpx.put(url, headers=self.headers, json=data)
        elif method == "delete":
            r = httpx.delete(url, headers=self.headers)
        else:
            raise Exception("Invalid method")
        
        self.debug_print(f"Response: {r.status_code}")
        return r

    def process_response(self, r: httpx.Response):
        if r.status_code == 200:
            try:
                return r.json()["data"]
            except KeyError:
                return r.json()
        else:
            raise Exception(f"\n\nSellpass error:\n\nEndpoint: {r.url}\nStatus code: {r.status_code}\nErrors: {r.json()['errors']}\nMessage: {r.json()['message']}")
    