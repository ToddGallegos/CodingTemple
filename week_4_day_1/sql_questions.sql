-- 1. How many actors are there with the last name ‘Wahlberg’?
-- 2
SELECT * FROM actor WHERE last_name = 'Wahlberg';

-- 2. How many payments were made between $3.99 and $5.99?
-- 3238
SELECT COUNT(*) FROM payment WHERE amount > 3.99 and amount < 5.99;

-- 3. What film does the store have the most of? (search in inventory)
-- film_id 350 ('Garden Island'), but there are a bunch of movies with 8 copies.
SELECT film_id, COUNT(film_id) FROM inventory GROUP BY film_id ORDER BY COUNT(*) DESC LIMIT 1;

SELECT film_id, title FROM film WHERE film_id = 350;

-- 4. How many customers have the last name ‘William’?
-- 0 customers have last name 'william'
SELECT * FROM customer WHERE last_name LIKE '%illiam%';

-- 5. What store employee (get the id) sold the most rentals?
-- staff_id 2 sold the most.
SELECT staff_id, SUM(amount) AS total FROM payment GROUP BY staff_id ORDER BY total DESC;

-- 6. How many different district names are there?
-- 378

SELECT (COUNT(DISTINCT district)) FROM address;

-- 7. What film has the most actors in it? (use film_actor table and get film_id)
--- Lambs Cincinatti
SELECT film_id, COUNT(DISTINCT actor_id) FROM film_actor GROUP BY film_id ORDER BY COUNT(DISTINCT actor_id) DESC;
SELECT * FROM film WHERE film_id = 508;

-- 8. From store_id 1, how many customers have a last name ending with ‘es’? (use customer table)
-- 21
SELECT COUNT(last_name) FROM customer WHERE last_name LIKE '%es';

-- 9. How many payment amounts (4.99, 5.99, etc.) had a number of rentals above 250 for customers
-- with ids between 380 and 430? (use group by and having > 250)
-- 3
SELECT amount, COUNT(amount) FROM payment WHERE customer_id > 379 AND customer_id < 431 GROUP BY amount ORDER BY COUNT(amount) DESC;

--SELECT amount, COUNT(amount) AS tot_count FROM payment WHERE customer_id > 379 AND customer_id < 431 AND tot_count > 250 GROUP BY amount ORDER BY COUNT(amount) DESC;

-- 10. Within the film table, how many rating categories are there? And what rating has the most
-- movies total?
-- 5 different ratings. PG-13 has the most at 223.

SELECT COUNT(DISTINCT rating) FROM film;

SELECT rating, COUNT(rating) FROM film GROUP BY rating ORDER BY COUNT(rating) DESC;