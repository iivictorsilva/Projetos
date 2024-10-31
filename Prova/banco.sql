-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS techstore;

-- Uso do banco de dados
USE techstore;

-- Criação da tabela para armazenar as solicitações de orçamento
CREATE TABLE IF NOT EXISTS solicitacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    details TEXT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);