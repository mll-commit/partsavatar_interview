import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT name, SUM(price*quantity) AS total_spend
    FROM Customers
    LEFT JOIN Orders USING(customer_id)
    LEFT JOIN Order_Items USING(order_id)
    GROUP BY 1
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
