import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent/"db.sqlite")
    cursor = db.cursor()

def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions(
        questionId INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        question TEXT,
        userId INTEGER
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category(
        categoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text)
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            picture TEXT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (category)
)"""
    )
    db.commit()
def populate_tables():
    cursor.execute(
        """
        INSERT INTO category(name)
        VALUES ('книги'), ('Сувениры'), ('Манга')
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, price, picture, categoryId)
        VALUES ('Анна Каренина', 2000.0, '/images/book.jpg'),
                ('Война и мир', 3000.0, '/images/book.jpg'),
                ('Мастер и Маргарита', 4000.0, '/images/book.jpg'),
                ('Герой нашего времени', 5000.0, '/images/boot.jpg')
        """
    )
    db.commit()

def get_products():
        cursor.execute(
            """
            SELECT * FROM products Join category ON product.categoryId = category.id
            """
        )
        return cursor.fetchall()
def get_products_by_category(categoryId):
    cursor.execute(
        """
        SELECT name FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()

def save_question(data):
    cursor.execute(
        """
        INSERT INTO questions (name, email, question, iserId)
        VALUES (:name, :email, :question, :user_id)
        """,
        {'n': data['name'],
         'e': data['email'],
         'question': data['question'],
         'user_id': user_id}
    )

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products_by_category(1))
