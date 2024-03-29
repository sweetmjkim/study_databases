-- - Table Customers 
-- - 조건 Country 가 Germany 와 USA가 아닌 것들
-- - 조건 : CustomerID가 50에서 89이고, City가 London 고객

SELECT * 
FROM Customers
WHERE (Country <> 'Germany') AND (Country <> 'USA')     -- COUNT : 67
;

SELECT * 
FROM Customers
WHERE CustomerID BETWEEN 50 AND 89
AND City = 'London'  
;