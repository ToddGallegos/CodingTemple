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