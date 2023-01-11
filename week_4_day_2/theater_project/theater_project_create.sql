CREATE TABLE customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    date_of_birth DATE,
    billing_info VARCHAR(150)
);

CREATE TABLE movie(
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    release_date DATE,
    rating VARCHAR(50),
    genre VARCHAR(50)
);

CREATE TABLE ticket(
    ticket_id SERIAL PRIMARY KEY,
    movie_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    date_sold TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(movie_id) REFERENCES movie(movie_id),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE concession(
    concession_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    concession_name VARCHAR(100),
    price NUMERIC(10, 2),
    quantity_sold INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);
