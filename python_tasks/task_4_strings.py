# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    final_string = sku_string.replace('-', ' ').title()
    return final_string

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
print(format_sku("brake-pads-ceramic"))
print(format_sku("engine-oil-10w30"))
