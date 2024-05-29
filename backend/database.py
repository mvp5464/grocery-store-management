from mysql.connector import Error
from sql_connection import get_sql_connection 

def create_table(cnx):
    try:
        cursor = cnx.cursor()

        create_uom_table_query = """ CREATE TABLE IF NOT EXISTS uom (
        uom_id INT AUTO_INCREMENT PRIMARY KEY,
        uom_name VARCHAR(45) NOT NULL
    );"""
        create_product_table_query = """ CREATE TABLE IF NOT EXISTS product (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        uom_id INT NOT NULL,
        price_per_unit DOUBLE NOT NULL,
        CONSTRAINT fk_uom_id FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
            ON UPDATE RESTRICT
            ON DELETE RESTRICT

    );"""
        create_order_table_query = """ CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(100) NOT NULL,
        total DOUBLE NOT NULL,
        datetime DATETIME NOT NULL
    );"""
        create_order_details_table_query = """ CREATE TABLE IF NOT EXISTS order_details (
        order_id INT PRIMARY KEY,
        product_id INT NOT NULL,
        quantity DOUBLE NOT NULL,
        total_price DOUBLE NOT NULL,
        CONSTRAINT fk_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id)
            ON UPDATE RESTRICT
            ON DELETE RESTRICT,
        CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product(product_id)
            ON UPDATE RESTRICT
            ON DELETE RESTRICT
    );"""
        cursor.execute(create_uom_table_query)
        cursor.execute(create_product_table_query)
        cursor.execute(create_order_table_query)
        cursor.execute(create_order_details_table_query)

        return "New Table Created"
    except Error as err:
        print("Error while creating tables: ", err)
    finally:
        if cursor:
            cursor.close()
   
def get_all_product(cnx):
    try:
        cursor = cnx.cursor()

        query = "SELECT product.product_id, product.name, product.uom_id, product.price_per_unit, uom.uom_name FROM product inner join uom on product.uom_id=uom.uom_id"
        
        response = []
        cursor.execute(query)
        for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
            response.append(
                {
                    'product_id': product_id,
                    'name': name,
                    'uom_id': uom_id,
                    'price_per_unit': price_per_unit,
                    'uom_name': uom_name
                }
            )
            print(product_id, name, uom_id, price_per_unit, uom_name)
        return response
    except Error as err:
        print("Error while fetching products: ", err)

    finally:
        if cursor:
            cursor.close()

def insert_uom(cnx, uom):
    try:
        cursor = cnx.cursor()
        query = "INSERT IGNORE INTO uom (uom_id, uom_name) VALUES (%s, %s)"
        data = (uom['uom_id'], uom['uom_name'])
        cursor.execute(query, data)
        cnx.commit()

        return "created new"

    except Error as err:
        print("Error while inserting new uom: ", err)
    finally:
        if cursor:
            cursor.close()

def insert_new_product(cnx, product):
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO product (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
        data = (product['product_name'],product['uom_id'],product['price_per_unit'])
        cursor.execute(query, data)
        cnx.commit()

        return cursor.lastrowid

    except Error as err:
        print("Error while inserting new product: ", err)
    finally:
        if cursor:
            cursor.close()

def delete_product(cnx,product_id):
    try:
        cursor = cnx.cursor()
        query = (f"DELETE FROM product where product_id={str(product_id)}")
        cursor.execute(query)
        cnx.commit()
        return "deleted"
    except Error as err:
        print("Error while deleting the product: ", err)
    finally:
        if cursor:
            cursor.close()

 
if __name__ == "__main__":
    try:
        cnx = get_sql_connection()
        print(create_table(cnx))
        print(insert_uom(cnx, {
            'uom_id':3,
            'uom_name':'litre'
        }))
        print(get_all_product(cnx))
        print(insert_new_product(cnx,{
            'product_name':'cabbage',
            'uom_id':'3',
            'price_per_unit':'10'
        }))
        print(delete_product(cnx,1))
    finally:
        if cnx:
            cnx.close()
