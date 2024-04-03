SELECT Customers.CustomerName, ORDERS_GROUP.CustomerID
FROM Customers
LEFT JOIN (SELECT CustomerID, COUNT(CustomerID) AS CNT
FROM Orders
GROUP BY CustomerID) AS ORDERS_GROUP
ON Customers.CustomerID=ORDERS_GROUP.CustomerID
ORDER BY Customers.CustomerName;

SELECT Customers.CustomerName, ORDERS_GROUP.CustomerID
FROM Customers
	LEFT JOIN (SELECT CustomerID, COUNT(CustomerID) AS CNT
				FROM Orders
				GROUP BY CustomerID
				) AS ORDERS_GROUP
	ON Customers.CustomerID=ORDERS_GROUP.CustomerID
WHERE ORDERS_GROUP.CustomerID IS NULL
ORDER BY Customers.CustomerName;