create table new_table(
	manufacturer_name varchar(30),
	model_name varchar(30),
	transmission varchar(30),
	color varchar(30),
	year_produced INT NOT NULL,
	engine_fuel varchar(30),
	engine_type varchar(30),
	body_type varchar(30),
	price_usd INT NOT NULL,
	location_region varchar(30)
);
--DROP TABLE new_table
select * from new_table
-- Запит 1: Назва виробника та ціна найдорожчого автомобіля
SELECT manufacturer_name, MAX(price_usd) AS max_car_price
FROM new_table
GROUP BY manufacturer_name;

-- Запит 2: Загальна кількість грошей, отриманих кожним виробником
SELECT manufacturer_name, SUM(price_usd) AS total_income
FROM new_table
GROUP BY manufacturer_name;

-- Запит 3: Залежність кількості проданих авто від кольору
SELECT color, COUNT(*) AS car_count
FROM new_table
GROUP BY color;

