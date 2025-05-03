DROP DATABASE IF EXISTS watch_db;
CREATE DATABASE IF NOT EXISTS watch_db;
USE watch_db;

DROP TABLE IF EXISTS `user`;
DROP VIEW IF EXISTS `user`;
CREATE TABLE user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS `address`;
DROP VIEW IF EXISTS `address`;
CREATE TABLE address(
    pincode INT PRIMARY KEY,
    user_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

DROP TABLE IF EXISTS `watch`;
DROP VIEW IF EXISTS `watch`;
CREATE TABLE watch(
    watch_id INT PRIMARY KEY NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    watch_desc VARCHAR(255) NOT NULL,
    watch_rating INT NOT NULL,
    year INT NOT NULL,
    price INT NOT NULL
);

DROP TABLE IF EXISTS `cart`;
DROP VIEW IF EXISTS `cart`;
CREATE TABLE cart(
    cart_id INT PRIMARY KEY NOT NULL,
    total_price INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

DROP TABLE IF EXISTS `cart_item`;
DROP VIEW IF EXISTS `cart_item`;
CREATE TABLE cart_item(
    cart_item_id INT PRIMARY KEY NOT NULL, -- what do you mean by cart_item_id??
    cart_id INT NOT NULL,
    user_id INT NOT NULL,
    watch_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (watch_id) REFERENCES watch(watch_id),
    FOREIGN KEY (cart_id) REFERENCES cart(cart_id)
);

DROP TABLE IF EXISTS `order`;
DROP VIEW IF EXISTS `order`;
CREATE TABLE `order`(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATETIME NOT NULL,
    total_price INT NOT NULL,
    user_id INT NOT NULL,
    order_status VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

DROP TABLE IF EXISTS `order_item`;
DROP VIEW IF EXISTS `order_item`;
CREATE TABLE order_item(
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    watch_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `order`(order_id),
    FOREIGN KEY (watch_id) REFERENCES watch(watch_id)
);

DROP TABLE IF EXISTS `payment`;
DROP VIEW IF EXISTS `payment`;
CREATE TABLE payment(
    payment_id INT PRIMARY KEY NOT NULL,
    payment_date DATETIME NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    total_price INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- INSERT INTO watch VALUES(

-- );