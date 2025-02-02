-- ЗАДАЧА 1
SELECT orderNumber,
    productCode,
    MAX(priceEach * quantityOrdered) as totalCost
FROM orderdetails
-- GROUP BY orderNumber,
    --     productCode
-- Group By не нужен, так как это PK, и таблица имеет >= 1 степень нормализации
ORDER BY totalCost DESC
LIMIT 10;
-- ЗАДАЧА 2
SELECT orderNumber,
    SUM(priceEach * quantityOrdered) as total
FROM orderdetails
GROUP BY orderNumber
HAVING total > 59000;
-- ЗАДАЧА 3
SELECT orders.orderNumber,
    orders.orderDate,
    orders.status,
    total_filtered.total as total
FROM (
        SELECT orderNumber,
            SUM(priceEach * quantityOrdered) as total
        FROM orderdetails
        GROUP BY orderNumber
        HAVING total > 59000
    ) AS total_filtered
    INNER JOIN orders ON total_filtered.orderNumber = orders.orderNumber;
-- ЗАДАЧА 4
SELECT customers.contactFirstName,
    customers.contactLastName,
    customers.country,
    total_filtered_exp.orderNumber,
    total_filtered_exp.orderDate,
    total_filtered_exp.status,
    total_filtered_exp.total
FROM(
        SELECT orders.customerNumber,
            orders.orderNumber,
            orders.orderDate,
            orders.status,
            total_filtered.total as total
        FROM (
                SELECT orderNumber,
                    SUM(priceEach * quantityOrdered) as total
                FROM orderdetails
                GROUP BY orderNumber
                HAVING total > 59000
            ) AS total_filtered
            INNER JOIN orders ON total_filtered.orderNumber = orders.orderNumber
    ) AS total_filtered_exp
    INNER JOIN customers ON customers.customerNumber = total_filtered_exp.customerNumber;
-- ЗАДАЧА 5
SELECT products.productName,
    total_code.total
FROM (
        SELECT productCode,
            SUM(priceEach * quantityOrdered) as total
        FROM orderdetails
        GROUP BY productCode
    ) AS total_code
    INNER JOIN products ON total_code.productCode = products.productCode
ORDER BY total_code.total DESC;
-- ЗАДАЧА 6
;
-- ЗАДАЧА 7
;