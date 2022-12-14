from sellpass import SellPass

api_key = "API Key from https://dashboard.sellpass.io/settings/security" # Replace with your API key

if __name__ == "__main__":
    sp = SellPass(api_key = api_key, debug = True, shop_id = None) # <--- Replace shop_id with your shop ID, if you have multiple shops

    print(f"Shop name: {sp.get_public_shop()[0]['shop']['name']}") # Get shop name

    customers = sp.get_customers() # Get all customers
    feedback = sp.get_feedback() # Get all feedback
    tickets = sp.get_tickets() # Get all tickets

    response = sp.create_announcement(
        title = "Test Announcement",
        short_description = "This is a test!",
        description = "This is a test announcement, showing of the SellPass API!",
        unlisted = False,
        private = False,
        button_text = "Use now!",
        button_link = "https://sellpass.io"
        ) # Create an announcement
    
    print(response)  
    # {
    #    'id': 1341,
    #    'path': 'yD7PV1W41MO2',
    #    'title': 'Test Announcement',
    #    'shortDescription': 'This is a test!',
    #    'description': 'This is a test announcement, showing of the SellPass API!',
    #    'buttonText': 'Use now!',
    #    'buttonLink': 'https://sellpass.io',
    #    'visibility': 0,
    #    'createdAt': '2022-12-08T15:37:00.4600125Z',
    #    'shopId': 4100
    # }
