-- SELECT CustomerName, ContactName, Address
-- FROM Customers
-- WHERE Address IS NOT NULL
-- ORDER BY CustomerName DESC
-- LIMIT 5, 2;

-- 실습하는 사이트 : https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_is_null

-- - 다음 조건은 subquery 사용
-- - Table : Customers, Orders
-- + 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
-- - Table : Orders
-- + 조건 : 주문 갯수가 20개 이상인 회사 LastName과 갯수
-- - Table : Suppliers
-- + 조건 : CategoryID를 가장 많이 제공 상위 2개 회사 정보

SELECT CustomerID, CustomerName
FROM Customers
WHERE CustomerID IN (SELECT CustomerID
				FROM Orders
				GROUP BY CustomerID
				HAVING COUNT(CustomerID) >= 5
				ORDER BY CustomerID ASC);
-- Number of Records: 72 

SELECT EmployeeID, LastName
FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID
				FROM Orders
				GROUP BY EmployeeID
				HAVING COUNT(EmployeeID) >= 20)
                ORDER BY COUNT(CustomerID) ASC;
-- Number of Records: 9

SELECT SupplierName, SupplierID
FROM Suppliers
where SupplierID in	(select SupplierID
    from (select SupplierID, count(SupplierID) as CNT
        from Products
        group by SupplierID
        order by CNT ASC
        limit 2) as sub_query);


-- 3번문제에 대한 답들
SELECT SupplierID, CategoryID, COUNT(CategoryID) AS CNT
FROM Products
WHERE 1 = 1		-- 사용하지않을때 이렇게 작성
GROUP BY CategoryID, SupplierID;

-- SUPPLIER MAX 상위 2개
SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) AS CNT
FROM ( SELECT SupplierID, CategoryID, COUNT(CategoryID) AS CNT
		FROM Products
		WHERE 1 = 1
		GROUP BY CategoryID, SupplierID
		) AS Category_GROUP
WHERE 1 = 1
GROUP BY Category_GROUP.SupplierID

-- SUPPLIERID
SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) AS CNT
FROM ( SELECT SupplierID, CategoryID, COUNT(CategoryID) CNT
	FROM Products
	WHERE 1 = 1
	GROUP BY SupplierID, CategoryID
	) AS Category_GROUP
WHERE 1 = 1
GROUP BY Category_GROUP.SupplierID
ORDER BY COUNT(Category_GROUP.SupplierID) DESC
LIMIT 0, 2 ;

SELECT *
FROM Suppliers
WHERE SupplierID = (
		SELECT Category_GROUP.SupplierID
		FROM ( SELECT SupplierID, CategoryID, COUNT(CategoryID) CNT
		FROM Products
		WHERE 1 = 1
		GROUP BY SupplierID, CategoryID
		) AS Category_GROUP
		WHERE 1 = 1
		GROUP BY Category_GROUP.SupplierID
		ORDER BY COUNT(Category_GROUP.SupplierID) DESC
		LIMIT 0, 2
);