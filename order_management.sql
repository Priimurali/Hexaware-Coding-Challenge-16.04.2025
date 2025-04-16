create database order_management;
use order_management; 


CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(10) CHECK (role IN ('Admin', 'User')) NOT NULL
);

-- PRODUCTS TABLE
CREATE TABLE Products (
    productId INT PRIMARY KEY,
    productName VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    quantityInStock INT NOT NULL,
    type VARCHAR(20) CHECK (type IN ('Electronics', 'Clothing')) NOT NULL
);

-- ELECTRONICS TABLE
CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(100),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

-- CLOTHING TABLE
CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(10),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

-- ORDERS TABLE
CREATE TABLE Orders (
    orderId INT IDENTITY(1,1) PRIMARY KEY,
    userId INT,
    orderDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (userId) REFERENCES Users(userId)
);


CREATE TABLE OrderDetails (
    orderDetailId INT IDENTITY(1,1) PRIMARY KEY,
    orderId INT,
    productId INT,
    quantity INT DEFAULT 1,
    FOREIGN KEY (orderId) REFERENCES Orders(orderId) ON DELETE CASCADE,
    FOREIGN KEY (productId) REFERENCES Products(productId)
);


select * from users;
select * from OrderDetails;
select * from Orders;
select * from Clothing;
select * from Electronics;
select * from products;



DELETE FROM Orders WHERE orderId = 2;
