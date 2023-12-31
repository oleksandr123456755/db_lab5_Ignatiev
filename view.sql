-- VIEW для результату першого запиту
CREATE VIEW manufacturer_max_car_price AS
SELECT m.name AS manufacturer_name, MAX(c.price) AS max_car_price
FROM manufacturer m
JOIN car c ON m.manufacturer_id = c.manufacturer_id
GROUP BY m.name;

-- VIEW для результату другого запиту
CREATE VIEW manufacturer_total_income AS
SELECT m.name AS manufacturer_name, SUM(c.price) AS total_income
FROM manufacturer m
JOIN car c ON m.manufacturer_id = c.manufacturer_id
GROUP BY m.name;

-- VIEW для результату третього запиту
CREATE VIEW car_color_count AS
SELECT color, COUNT(*) AS car_count
FROM car
GROUP BY color;

SELECT * FROM manufacturer_max_car_price
SELECT * FROM manufacturer_total_income
SELECT * FROM car_color_count