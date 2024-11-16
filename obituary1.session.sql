CREATE TABLE obituaries
(
    id INT
    AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR
    (100) NOT NULL,
    date_of_birth DATE,
    date_of_death DATE,
    obituary_text TEXT,
    image VARCHAR
    (255)
);