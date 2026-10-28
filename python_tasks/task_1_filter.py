# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.

def filter_orders(order_ids):
    final_list = []
    for c in order_ids:
        if c > 100 and c%2 == 0:
            final_list.append(c)
    return sorted(final_list, reverse=True)

# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]
# Expected Output: [300, 202, 120, 110]
print(filter_orders(test_data))
