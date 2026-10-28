import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    WITH sum_table AS (
    SELECT sku, SUM(quantity) AS total
    FROM Order_Items
    GROUP BY 1)

    SELECT sku
    FROM sum_table
    WHERE total > 1
    """
    
    cursor.execute(query)
    return cursor.fetchall()
