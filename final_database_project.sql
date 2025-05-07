-- Library Management System Database
CREATE DATABASE lmsd;

USE lmsd;

CREATE TABLE Author (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INT,
    UNIQUE (name, birth_year)
);

CREATE TABLE Book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publication_year INT,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE BookCategory (
    book_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Member (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    join_date DATE NOT NULL
);

CREATE TABLE Loan (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT loan_unique UNIQUE (member_id, book_id, loan_date)
);

INSERT INTO Author (name, birth_year) VALUES 
('J.K. Rowling', 1965),
('George Orwell', 1903),
('Jane Austen', 1775);

INSERT INTO Book (title, publication_year, isbn, author_id) VALUES 
('Harry Potter', 1997, '9780747532699', 1),
('1984', 1949, '9780451524935', 2),
('Pride and Prejudice', 1813, '9780141439518', 3);

INSERT INTO Category (name) VALUES 
('Fiction'),
('Fantasy'),
('Classic'),
('Dystopian');

INSERT INTO BookCategory (book_id, category_id) VALUES 
(1, 1),
(1, 2),
(2, 1),
(2, 4), 
(3, 1), 
(3, 3); 

INSERT INTO Member (name, email, join_date) VALUES 
('Alice Kimanzi', 'alice@gmail.com', '2024-01-15'),
('Bob mutua', 'bob@gmail.com', '2024-02-10');

INSERT INTO Loan (member_id, book_id, loan_date, due_date, return_date) VALUES 
(1, 1, '2024-03-01', '2024-03-15', '2024-03-14'),
(2, 2, '2024-03-05', '2024-03-19', NULL);
