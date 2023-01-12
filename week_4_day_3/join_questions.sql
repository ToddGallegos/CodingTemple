-- 1. List all customers who live in Texas (use
-- JOINs)

SELECT first_name, last_name, district
FROM customer
FULL JOIN address
ON customer.address_id = address.address_id
WHERE address.district = 'Texas';

-- 2. Get all payments above $6.99 with the Customer's Full
-- Name

SELECT first_name, last_name, amount
FROM payment
FULL JOIN customer
ON payment.customer_id = customer.customer_id
WHERE amount > 6.99
GROUP BY customer.first_name, customer.last_name, amount;

-- 3. Show all customers names who have made payments over $175(use
-- subqueries)

SELECT first_name, last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    WHERE amount > 175
);

-- 4. List all customers that live in Nepal (use the city
-- table)

-- NONE LIVE IN NEPAL
SELECT *
FROM city
WHERE city LIKE '%epal%';


-- 5. Which staff member had the most
-- transactions?

-- Jon Stephens
SELECT staff.staff_id, first_name, last_name, COUNT(payment.payment_id) AS transactions
FROM staff
JOIN payment
ON payment.staff_id = staff.staff_id
GROUP BY staff.staff_id, first_name, last_name
ORDER BY transactions DESC;

-- 6. How many movies of each rating are
-- there?

SELECT rating, COUNT(rating) AS total
FROM film
GROUP BY rating
ORDER BY total DESC;

-- 7.Show all customers who have made a single payment
-- above $6.99 (Use Subqueries)

SELECT first_name, last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    WHERE amount > 6.99
);

-- 8. How many free rentals did our store give away?
--NONE

SELECT *
FROM payment
WHERE amount = 0