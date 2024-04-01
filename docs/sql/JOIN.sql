-- JOIN
SELECT *
FROM Products INNER JOIN Suppliers
	ON Suppliers.SupplierID = Products.SupplierID
    AND SupplierName IN ('Exotic Liquid', 'Tokyo Traders')
;

SELECT PRODUCT.SupplierID, SUPPLIER.SupplierID
FROM Products AS PRODUCT INNER JOIN Suppliers AS SUPPLIER
	ON SUPPLIER.SupplierID = PRODUCT.SupplierID
    AND SupplierName IN ('Exotic Liquid', 'Tokyo Traders')
;

SELECT Categories.*, PRODUCT.*, SUPPLIER.*
FROM Products AS PRODUCT INNER JOIN Suppliers AS SUPPLIER
	ON SUPPLIER.SupplierID = PRODUCT.SupplierID
    AND SupplierName IN ('Exotic Liquid', 'Tokyo Traders')
     INNER JOIN Categories
        ON PRODUCT.CategoryID = Categories.CategoryID
;