#!/usr/bin/env python



 Suppose that a website contains two tables, the Customers table and the Orders table.
 Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

1. Assume no dup in Customers Table
2. Assume returned name list is not ordered
3. Assume Orders Table has dups

SELECT
  name
FROM
  Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders GROUP BY CustomerId)
;

SELECT
  t1.name
FROM
  (SELECT
     Id AS customer_id,
     Name As name,
   FROM Customers) AS t1
  JOIN
  (SELECT
     CustomerId as customer_id
   FROM Orders) AS t2
  ON
    t1.customer_id == t2.customer_id;
