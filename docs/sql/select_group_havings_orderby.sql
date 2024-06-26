-- - Table : Products
-- + 조건 : CategoryID 가 10개 이상
-- - Table : Customers, Orders
-- + 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
-- - Table : Orders, ?
-- + 조건 : 20개 이상 주문 받은 회사 LastName 과 갯수

SELECT COUNT(CategoryID) AS CNT, CategoryID
FROM Products
GROUP BY CategoryID
HAVING COUNT(CategoryID) >= 10
;
-- COUNT : 5 / CategoryID : 1, 2, 3, 4, 8

SELECT COUNT(CustomerID) AS CNT, CustomerID
FROM Orders
GROUP BY CustomerID
HAVING COUNT(CustomerID) >= 5;
ORDER BY CustomerID ASC;
-- COUNT : 9 / CustomerID : 20, 37, 41, 46, 51, 63, 65, 75, 87
SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (20, 37, 41, 46, 51, 63, 65, 75, 87);

2-1. 같은 결과(subquery)
SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (SELECT CustomerID
				FROM Orders
				GROUP BY CustomerID
				HAVING COUNT(CustomerID) >= 5
				ORDER BY CustomerID ASC);

2-2. 같은 결과(subquery)
SELECT SUB_ORDERS.CNT, SUB_ORDERS.CustomerID
FROM (
		SELECT COUNT(CustomerID) AS CNT, CustomerID
		FROM Orders
		GROUP BY CustomerID
		HAVING COUNT(CustomerID) >= 5
		ORDER BY CustomerID ASC
) AS SUB_ORDERS
;


SELECT COUNT(EmployeeID) AS CNT, EmployeeID
FROM Orders
GROUP BY EmployeeID
HAVING COUNT(EmployeeID) >= 20;
ORDER BY EmployeeID ASC;
-- COUNT : 5 / EmployeeID : 1, 2, 3, 4, 8
SELECT EmployeeID, LastName
FROM Employees
WHERE EmployeeID IN (1, 2, 3, 4, 8);