INSERT INTO customer(
    first_name,
    last_name,
    email,
    date_of_birth,
    billing_info
) VALUES (
    'Tom',
    'Smith',
    'tom.smith@example.com',
    '1990-01-01',
    'VISA 0483 exp. 01/30 zip 90210'
), (
    'Jill',
    'Hernandez',
    'jillyherny@emails.com',
    '1999-12-25',
    'cash'
), (
    'Billy',
    'Jackson',
    'billyjack@oldmovie.com',
    '1975-06-07',
    'MASTERCARD 5761 exp. 06/27 zip 95959'
);

INSERT INTO movie(
    title,
    release_date,
    rating,
    genre
) VALUES (
    'Big Movie 1',
    '2022-12-29',
    'PG-13',
    'action'
), (
    'Biggest Movie 2',
    '2023-01-10',
    'R',
    'drama'
), (
    'Sappy Movie 3',
    '2022-12-24',
    'PG-13',
    'romance'
);

INSERT INTO ticket(
    movie_id,
    customer_id
) VALUES (
    1,
    1
), (
    2,
    2
), (
    3,
    3
);

INSERT INTO concession(
    customer_id,
    concession_name,
    price,
    quantity_sold
) VALUES (
    1,
    'popcorn',
    9.99,
    2
), (
    2,
    'soda',
    8.99,
    3
), (
    3,
    'licorice',
    7.99,
    1
);
