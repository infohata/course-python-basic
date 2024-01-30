-- DROP TABLE orders;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    total DECIMAL(18,2),
    client_id INTEGER REFERENCES clients(id)
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    price DECIMAL(18,2)
);

CREATE TABLE order_line (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES product(id),
    quantity FLOAT DEFAULT 1 NOT NULL
);

INSERT INTO orders (date, total, client_id)
    VALUES (DATE("2024-01-29"), 100.00, 1);
INSERT INTO orders (date, total, client_id)
    VALUES (DATE("2024-01-25"), 20.00, 3);
INSERT INTO orders (date, total, client_id)
    VALUES (DATE("2023-11-24"), 14.05, 4);
INSERT INTO orders (date, total, client_id)
    VALUES (DATE("2023-12-18"), 77.77, 5);
INSERT INTO orders (date, total, client_id)
    VALUES (DATE("2023-10-10"), 115.11, 1);

INSERT INTO product (name, price)
    VALUES ("Gel Battery 80Ah 12V", 100);
INSERT INTO product (name, price)
    VALUES ("Netflix 1 Month subscription", 10);
INSERT INTO product (name, price)
    VALUES ("Cables", 15.11);

INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (1, 1, 1);
INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (2, 2, 2);
INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (3, 2, 3);
INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (4, 1, 1);
INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (5, 1, 1);
INSERT INTO order_line (order_id, product_id, quantity) 
    VALUES (5, 3, 1);

SELECT * FROM orders;

SELECT orders.id, date, total, first_name, last_name 
    FROM orders, clients
    WHERE orders.client_id = clients.id;

SELECT SUM(total), first_name, last_name 
    FROM orders JOIN clients
    ON orders.client_id = clients.id
    GROUP BY client_id
    ORDER BY SUM(total) DESC;

SELECT orders.id, product.name, quantity, product.price, 
    product.price * quantity AS line_total
    FROM order_line
    JOIN orders ON order_id = orders.id
    JOIN product ON product_id = product.id;

SELECT orders.id, first_name, last_name,
    orders.total || " €" AS order_total,
    SUM(quantity * price) || " €" AS prod_total,
    SUM(quantity) AS qty, 
    (SUM(quantity * price) - orders.total) AS disc_eur,
    ROUND((SUM(quantity * price) - orders.total) / 
        SUM(quantity * price) * 100, 2) AS discount
    FROM order_line 
    JOIN orders ON order_id = orders.id
    JOIN product ON product_id = product.id
    JOIN clients ON client_id = clients.id
    GROUP BY order_id
    HAVING disc_eur > 0
    ORDER BY discount DESC
    ;

SELECT * FROM order_line 
    JOIN orders ON order_id = orders.id
    JOIN product ON product_id = product.id
    JOIN clients ON client_id = clients.id
    ;
