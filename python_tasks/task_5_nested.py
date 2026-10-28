# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    if "specs" in vehicle:
        d1 = vehicle["specs"]
    else:
        return "Unknown"
    if "model_info" in d1:
        d2 = d1["model_info"]
    else:
        return "Unknown"
    if "year" in d2:
        return d2["year"]
    else:
        return "Unknown"

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
