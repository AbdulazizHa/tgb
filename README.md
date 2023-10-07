'''CREATE TABLE IF NOT EXISTS product (
    productId INTEGER AUTOINCREMENT PRIMARY KEY,
    name TEXT,
    price FLOAT
    picture TEXT,
) '''

'''
INSERT INTO product (name, price, picture)
VALUES ('Анна Каренина', 2000.0, '/images/book.jpg'),
        ('Война и мир', 3000.0, '/images/book.jpg')
'''