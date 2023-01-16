-- creating the 7 tables needed for the car_dealership database:

CREATE TABLE car (
  car_id SERIAL,
  make VARCHAR(50),
  model VARCHAR(50),
  model_year INTEGER,
  PRIMARY KEY (car_id)
);

CREATE TABLE customer (
  customer_id SERIAL,
  customer_name VARCHAR(200),
  PRIMARY KEY (customer_id)
);

CREATE TABLE service_ticket (
  service_ticket_id SERIAL,
  car_id INTEGER NOT NULL,
  service_description VARCHAR(500) NOT NULL,
  PRIMARY KEY (service_ticket_id),
  FOREIGN KEY (car_id) REFERENCES car(car_id)
);

CREATE TABLE salesperson (
  salesperson_id SERIAL,
  salesperson_name VARCHAR(200),
  PRIMARY KEY (salesperson_id)
);

CREATE TABLE invoice (
  invoice_id SERIAL,
  salesperson_id INTEGER NOT NULL,
  car_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (salesperson_id) REFERENCES salesperson(salesperson_id),
  FOREIGN KEY (car_id) REFERENCES car(car_id),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE mechanic (
  mechanic_id SERIAL,
  mechanic_name VARCHAR(200),
  PRIMARY KEY (mechanic_id)
);

CREATE TABLE service_ticket_mechanic (
  service_ticket_mechanic_id SERIAL,
  service_ticket_id INTEGER NOT NULL,
  mechanic_id INTEGER NOT NULL,
  PRIMARY KEY (service_ticket_mechanic_id),
  FOREIGN KEY (service_ticket_id) REFERENCES service_ticket(service_ticket_id),
  FOREIGN KEY (mechanic_id) REFERENCES mechanic(mechanic_id)
);
