# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    final_dic={}
    for w in data:
        final_dic[w]=data.count(w)
    return final_dic

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))
