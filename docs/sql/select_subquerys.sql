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

SELECT EmployeeID, LastName
FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID
				FROM Orders
				GROUP BY EmployeeID
				HAVING COUNT(EmployeeID) >= 20)
                ORDER BY COUNT(CustomerID) ASC;

SELECT SupplierName, SupplierID
FROM Suppliers
where SupplierID in
	(select SupplierID
    from (
    	select SupplierID, count(SupplierID) as CNT
        from Products
        group by SupplierID
        order by CNT ASC
        limit 2
        ) as sub_query
    );