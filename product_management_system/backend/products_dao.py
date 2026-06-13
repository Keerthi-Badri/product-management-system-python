from sql_connection import get_sql_connection

print("PRODUCTS DAO FILE LOADED")  

# ---------------------------
# GET ALL PRODUCTS
# ---------------------------
def get_all_products(connection):
    cursor = connection.cursor(dictionary=True)

    query = """
SELECT products.product_id,
       products.name,
       products.uom_id,
       products.price_per_unit,
       uom.uom_name
FROM products
INNER JOIN uom
ON products.uom_id = uom.uom_id
"""

    cursor.execute(query)

    response = []
    for row in cursor:
        response.append(row)

    return response


# ---------------------------
# INSERT PRODUCT
# ---------------------------
def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = """
    INSERT INTO products (name, uom_id, price_per_unit)
    VALUES (%s, %s, %s)
    """

    name = product.get('product_name') or product.get('name')
    uom_id = product.get('uom_id')
    price = product.get('price_per_unit')

    if not name or not uom_id or not price:
        raise Exception(f"Invalid product payload: {product}")

    cursor.execute(query, (name, uom_id, price))
    connection.commit()

    return cursor.lastrowid


# ---------------------------
# DELETE PRODUCT
# ---------------------------
def delete_product(connection, product_id):
    cursor = connection.cursor()

    query = """
    DELETE FROM products WHERE product_id = %s
    """

    cursor.execute(query, (product_id,))
    connection.commit()

    return product_id


# ---------------------------
# TEST CODE (OPTIONAL)
# ---------------------------
if __name__ == '__main__':

    from sql_connection import get_sql_connection

    connection = get_sql_connection()

    print(get_all_products(connection))

    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': 1,
        'price_per_unit': 10
    }))