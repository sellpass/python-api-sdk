# Sellpass Python SDK
<img src="https://sellpass.io/img/logo.svg" width=350><img/>

## Information
- Python SDK for the **[Official Sellpass Api](https://docs.sellpass.io)**
- For all functions **[check this out](https://github.com/sellpass/python-api-sdk/blob/main/sellpass/__init__.py)**

## Requirements
- **[Python 3.7+](https://www.python.org/downloads/)**

## Installation (Windows)
- Open Command Prompt
- Run the following commands:
```
python3 -m pip install sellpass
```
- You are good to go!

## Example Usage
```python
from sellpass import SellPass

api_key = "API Key from https://dashboard.sellpass.io/settings/security" # Replace with your API key

if __name__ == "__main__":
    sp = SellPass(
        api_key = api_key,
        debug = True,
        shop_id = None # <--- Replace shop_id with your shop ID, if you have multiple shops
        )

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
```
## From Sellpass
- **[Official Site](https://sellpass.io)**
- **[Official Api Documentation](https://docs.sellpass.io)**
