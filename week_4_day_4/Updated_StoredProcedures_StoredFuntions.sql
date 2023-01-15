-- Explore Data with SELECT ALL statement
SELECT *
FROM payment;

-- Stored Procedure Example
-- Simulating a late fee charge

CREATE OR REPLACE PROCEDURE latefee(
	customer INTEGER,
	lateFeeAmount DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
	-- Add late fee to customer payment amount
	UPDATE payment
	SET amount = amount + lateFeeAmount
	WHERE customer_id = customer;
	
	-- Commit the above statement inside of a transaction
	COMMIT;
	
END;
$$



-- Calling a Stored Procedure
CALL lateFee(341,2.00);


-- Validate the late fee has been posted
SELECT *
FROM payment
WHERE customer_id = 341;

-- DELETE/DROP newly created stored procedure
DROP PROCEDURE latefee;





--- Stored Functions Example
-- Stored Function to insert data into the actor table

CREATE OR REPLACE FUNCTION add_actor(_actor_id INTEGER, _first_name VARCHAR, _last_name VARCHAR, _last_update TIMESTAMP WITHOUT TIME ZONE)
RETURNS void 
AS $MAIN$
BEGIN
	INSERT INTO actor(actor_id,first_name,last_name,last_update)
	VALUES(_actor_id, _first_name, _last_name, _last_update);
END;
$MAIN$
LANGUAGE plpgsql;

--Bad Call of Function
-- CALL add_actor(500,'Kevin', 'Hart', CURRENT_TIMESTAMP);

-- Good Call of Function
SELECT add_actor(500,'Kevin', 'Hart', NOW()::timestamp);

-- Verify that new actor has been added
SELECT *
FROM actor
WHERE actor_id = 500;


-- DELETE/DROP Stored Function
DROP FUNCTION add_actor;