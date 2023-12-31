CREATE OR REPLACE FUNCTION insert_test_data()
RETURNS VOID AS $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 10 LOOP
        INSERT INTO location (region_name, location_id)
        VALUES ('City ' || i, i+3); -- Приклад даних для вставки
        --delete from location where location_id=i+3 or location_id=100+i;
        i := i + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT insert_test_data();
select * from location