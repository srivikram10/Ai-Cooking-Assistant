CREATE DATABASE ai_cooking;

USE ai_cooking;

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query VARCHAR(255),
    recipe TEXT
);
