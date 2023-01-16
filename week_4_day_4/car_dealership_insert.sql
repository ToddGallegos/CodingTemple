-- TODO: USE STORED FUNCTIONS TO INSERT 2 PIECES OF DATA.

INSERT INTO car(
    make,
    model,
    model_year
) VALUES (
    'Kia',
    'Rio',
    2020
), (
    'Toyota',
    'Highlander',
    2021
), (
    'Honda',
    'Civic',
    2015
);

INSERT INTO customer(
    customer_name
) VALUES (
    'Tom Gallo'
), (
    'Crissy Dumas'
), (
    'Donald Garafalo'
);

INSERT INTO salesperson(
    salesperson_name
) VALUES (
    'Luke Harris'
), (
    'Ben Weathersby'
), (
    'Josh Hobbs'
);

INSERT INTO mechanic(
    mechanic_name
) VALUES (
    'Jon Jones'
), (
    'Daniel Cormier'
), (
    'Dustin Poirier'
);

INSERT INTO invoice(
    salesperson_id,
    car_id,
    customer_id
) VALUES (
    1,
    1,
    1
), (
    2,
    2,
    2
), (
    3,
    3,
    3
);

INSERT INTO service_ticket(
    car_id,
    service_description
) VALUES (
    1,
    'Oil Change'
), (
    2,
    'Splash shield replacement'
), (
    3,
    '20,000 mile tune-up'
);

INSERT INTO service_ticket_mechanic(
    service_ticket_id,
    mechanic_id
) VALUES (
    1,
    1
), (
    2,
    1
), (
    2,
    2
), (
    2,
    3
), (
    3,
    3
), (
    3,
    2
);

CREATE OR REPLACE PROCEDURE add_car(
    c_id INTEGER,
    _make VARCHAR(50),
    _model VARCHAR(50),
    _model_year INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO car(
    car_id,
    make,
    model,
    model_year
    ) VALUES (
        c_id,
        _make,
        _model,
        _model_year
    );
    COMMIT;

END;
$$

SELECT * FROM car;

CALL add_car(4, 'Chevy', 'Camaro', 1969);

CREATE OR REPLACE FUNCTION add_customer(
    c_id INTEGER,
    _customer_name VARCHAR(200)
)
RETURNS void
AS $MAIN$
BEGIN
    INSERT INTO customer(
        customer_id,
        customer_name
    ) VALUES (
        c_id,
        _customer_name
    );

END;
$MAIN$
LANGUAGE plpgsql;

SELECT * FROM customer;

SELECT add_customer(4, 'Mark Kistler');