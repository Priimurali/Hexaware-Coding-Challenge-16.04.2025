from .i_order_management_repository import IOrderManagementRepository
from util.db_conn_util import get_db_connection
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException

class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def create_user(self, user):
        self.cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", user.user_id, user.username, user.password, user.role)
        self.conn.commit()

    def create_product(self, user, product):
        if user.role != 'Admin':
            raise PermissionError("Only Admin can create products.")
        self.cursor.execute("INSERT INTO Products VALUES (?, ?, ?, ?, ?, ?)",
                            product.product_id, product.product_name, product.description,
                            product.price, product.quantity_in_stock, product.type)
        self.conn.commit()

    def create_order(self, user, products):
        self.cursor.execute("SELECT * FROM Users WHERE userId=?", user.user_id)
        if not self.cursor.fetchone():
            self.create_user(user)
        self.cursor.execute("INSERT INTO Orders (userId) OUTPUT Inserted.orderId VALUES (?)", user.user_id)
        order_id = self.cursor.fetchone()[0]
        for p in products:
            self.cursor.execute("INSERT INTO OrderDetails (orderId, productId, quantity) VALUES (?, ?, ?)",order_id, p.product_id, 1)

        self.conn.commit()

    def cancel_order(self, user_id, order_id):
        self.cursor.execute("SELECT * FROM Orders WHERE orderId=? AND userId=?", order_id, user_id)
        if not self.cursor.fetchone():
            raise OrderNotFoundException("Order or User not found")
        self.cursor.execute("DELETE FROM Orders WHERE orderId=?", order_id)
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()

    def get_order_by_user(self, user):
        self.cursor.execute("SELECT * FROM Orders WHERE userId=?", user.user_id)
        return self.cursor.fetchall()
