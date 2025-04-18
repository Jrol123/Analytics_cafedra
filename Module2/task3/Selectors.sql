-- модели принтеров с максимальной ценой
SELECT model,
    price
FROM Printer
WHERE price = (
        SELECT MAX(price)
        FROM Printer
    );

-- Средняя скорость ПК
SELECT AVG(speed)
FROM PC;

-- Производители, у которых есть ПК, но не ноутбуки
SELECT DISTINCT maker 
FROM Product 
WHERE type = 'PC' 
AND maker NOT IN (SELECT maker FROM Product WHERE type = 'Laptop');

-- Нахождение дубликатов
WITH duplicates AS (
    SELECT *, 
    ROW_NUMBER() OVER (PARTITION BY model, speed, ram, hd, cd, price ORDER BY code) AS rn
    FROM PC
)
SELECT * FROM duplicates WHERE rn > 1;

-- Изменение названия столбца
ALTER TABLE Printer RENAME COLUMN color TO color_type;
-- Изменение типа столбца
ALTER TABLE Printer ALTER COLUMN color_type TYPE VARCHAR(3);

-- ПК и ноутбуки с ram равной 64 и ценой больше 500
SELECT model, speed, ram, hd, price FROM PC 
WHERE price > 500 AND ram = 64
UNION ALL
SELECT model, speed, ram, hd, price FROM Laptop 
WHERE price > 500 AND ram = 64;