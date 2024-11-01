CREATE DATABASE produtos;

USE produtos;

CREATE TABLE produtos(

        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        description TEXT

);



