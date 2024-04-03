"+ 조건 : 비 진성고객 리스트 필요
+ 조건 : 판매자 중 수익 낮은 순위자 3명 정보, 총 판매액
+ 조건 : 배송 회사별 총 배송 건수와 총 제품 금액 정보
+ 조건 : 제품 회사별 총 판매액과 정보
+ 조건 : 카테고리별 판매 합계 정보+"

SELECT CustomerName
FROM Customers
WHERE CustomerID NOT IN (
select CustomerID FROM Orders
group by CustomerID
having count(OrderID) >=1)
;

SELECT Employees.EmployeeID, Employees.LastName, Employees.FirstName, Employees.BirthDate
	, sum(Products.Price*OrderDetails.Quantity) as TotalPrice
FROM Employees
left join Orders on Employees.EmployeeID = Orders.EmployeeID
left join OrderDetails on Orders.OrderID = OrderDetails.OrderID
left join Products on OrderDetails.ProductID = Products.ProductID
group by EmployeeID
order by TotalPrice ASC
limit 3
;

SELECT ShipperName, count(Orders.OrderID) as TotalDelivery ,sum(Products.Price*OrderDetails.Quantity) as TotalPrice
FROM Shippers
left join Orders on Shippers.ShipperID = Orders.ShipperID
left join OrderDetails on Orders.OrderID = OrderDetails.OrderID
left join Products on OrderDetails.ProductID = Products.ProductID
group by Shippers.ShipperName
order by Shippers.ShipperID ASC
;

SELECT Suppliers.SupplierID, Suppliers.SupplierName
		, sum((Products.Price)*(OrderDetails.Quantity)) as TotalPrice
FROM Suppliers
LEFT JOIN Products ON Suppliers.SupplierID = Products.SupplierID
LEFT JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
group by SupplierName
order by TotalPrice ASC
;

SELECT Categories.CategoryID, Categories.CategoryName
	,sum(Products.Price * OrderDetails.Quantity) as TotalPrice
FROM Categories
left join Products on Categories.CategoryID = Products.CategoryID
left join OrderDetails on Products.ProductID = OrderDetails.ProductID
group by CategoryID
order by Categories.CategoryID ASC
;