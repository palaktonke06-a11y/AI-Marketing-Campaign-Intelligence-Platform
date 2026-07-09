-- ==========================================
-- 1. Total Customers
-- ==========================================

SELECT COUNT(*) AS Total_Customers
FROM customers;


-- ==========================================
-- 2. Active Customers
-- ==========================================

SELECT COUNT(*) AS Active_Customers
FROM customers
WHERE Is_Active = 'Yes';


-- ==========================================
-- 3. Total Revenue
-- ==========================================

SELECT SUM(Net_Amount) AS Total_Revenue
FROM transactions;


-- ==========================================
-- 4. Total Transactions
-- ==========================================

SELECT COUNT(*) AS Total_Transactions
FROM transactions;


-- ==========================================
-- 5. Average Order Value
-- ==========================================

SELECT ROUND(AVG(Net_Amount),2) AS Avg_Order_Value
FROM transactions;


-- ==========================================
-- 6. Top 10 Customers by Spending
-- ==========================================

SELECT
    Customer_ID,
    SUM(Net_Amount) AS Total_Spent
FROM transactions
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;


-- ==========================================
-- 7. Top 10 Products by Revenue
-- ==========================================

SELECT
    Product_ID,
    SUM(Net_Amount) AS Revenue
FROM transactions
GROUP BY Product_ID
ORDER BY Revenue DESC
LIMIT 10;


-- ==========================================
-- 8. Revenue by Payment Method
-- ==========================================

SELECT
    Payment_Method,
    SUM(Net_Amount) AS Revenue
FROM transactions
GROUP BY Payment_Method
ORDER BY Revenue DESC;


-- ==========================================
-- 9. Revenue by Order Status
-- ==========================================

SELECT
    Order_Status,
    SUM(Net_Amount) AS Revenue
FROM transactions
GROUP BY Order_Status;


-- ==========================================
-- 10. Customer Segment Distribution
-- ==========================================

SELECT
    Customer_Segment,
    COUNT(*) AS Customers
FROM customers
GROUP BY Customer_Segment
ORDER BY Customers DESC;

-- ==========================================
-- 11. Top 10 Campaigns by Revenue
-- ==========================================

SELECT
    c.Campaign_Name,
    SUM(t.Net_Amount) AS Revenue
FROM campaigns c
JOIN transactions t
ON c.Campaign_ID = t.Campaign_ID
GROUP BY c.Campaign_Name
ORDER BY Revenue DESC
LIMIT 10;


-- ==========================================
-- 12. Campaign-wise Transactions
-- ==========================================

SELECT
    c.Campaign_Name,
    COUNT(t.Transaction_ID) AS Total_Transactions
FROM campaigns c
LEFT JOIN transactions t
ON c.Campaign_ID = t.Campaign_ID
GROUP BY c.Campaign_Name
ORDER BY Total_Transactions DESC;


-- ==========================================
-- 13. ROI of Each Campaign
-- ==========================================

SELECT
    Campaign_Name,
    Revenue,
    Spend,
    ROUND(((Revenue - Spend) / Spend) * 100,2) AS ROI
FROM campaigns
ORDER BY ROI DESC;


-- ==========================================
-- 14. Revenue by Product Category
-- ==========================================

SELECT
    p.Category,
    SUM(t.Net_Amount) AS Revenue
FROM products p
JOIN transactions t
ON p.Product_ID = t.Product_ID
GROUP BY p.Category
ORDER BY Revenue DESC;


-- ==========================================
-- 15. Top 10 Products Sold
-- ==========================================

SELECT
    p.Product_Name,
    SUM(t.Quantity) AS Units_Sold
FROM products p
JOIN transactions t
ON p.Product_ID = t.Product_ID
GROUP BY p.Product_Name
ORDER BY Units_Sold DESC
LIMIT 10;


-- ==========================================
-- 16. Revenue by Customer Segment
-- ==========================================

SELECT
    c.Customer_Segment,
    SUM(t.Net_Amount) AS Revenue
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Customer_Segment
ORDER BY Revenue DESC;


-- ==========================================
-- 17. Revenue by Gender
-- ==========================================

SELECT
    c.Gender,
    SUM(t.Net_Amount) AS Revenue
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Gender;


-- ==========================================
-- 18. Revenue by Age Group
-- ==========================================

SELECT
    c.Age_Group,
    SUM(t.Net_Amount) AS Revenue
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Age_Group
ORDER BY Revenue DESC;


-- ==========================================
-- 19. Top Performing Marketing Channels
-- ==========================================

SELECT
    Marketing_Channel,
    SUM(Revenue) AS Revenue
FROM campaigns
GROUP BY Marketing_Channel
ORDER BY Revenue DESC;


-- ==========================================
-- 20. Highest AI Campaign Scores
-- ==========================================

SELECT
    Campaign_Name,
    AI_Campaign_Score,
    Expected_ROI
FROM campaigns
ORDER BY AI_Campaign_Score DESC
LIMIT 10;

-- ==========================================
-- 21. Customer Lifetime Value (CLV)
-- ==========================================

SELECT
    c.Customer_ID,
    CONCAT(c.First_Name,' ',c.Last_Name) AS Customer_Name,
    SUM(t.Net_Amount) AS Lifetime_Value
FROM customers c
JOIN transactions t
ON c.Customer_ID = t.Customer_ID
GROUP BY c.Customer_ID, Customer_Name
ORDER BY Lifetime_Value DESC
LIMIT 10;


-- ==========================================
-- 22. Repeat Customers
-- ==========================================

SELECT
    Customer_ID,
    COUNT(Transaction_ID) AS Orders
FROM transactions
GROUP BY Customer_ID
HAVING Orders > 1
ORDER BY Orders DESC;


-- ==========================================
-- 23. Monthly Revenue Trend
-- ==========================================

SELECT
    YEAR(Transaction_Date) AS Year,
    MONTH(Transaction_Date) AS Month,
    SUM(Net_Amount) AS Revenue
FROM transactions
GROUP BY Year, Month
ORDER BY Year, Month;


-- ==========================================
-- 24. Best Performing Campaign Type
-- ==========================================

SELECT
    Campaign_Type,
    SUM(Revenue) AS Revenue,
    AVG(Expected_ROI) AS Avg_ROI
FROM campaigns
GROUP BY Campaign_Type
ORDER BY Revenue DESC;


-- ==========================================
-- 25. Conversion Funnel Analysis
-- ==========================================

SELECT
    Funnel_Stage,
    COUNT(*) AS Campaigns,
    AVG(Success_Probability) AS Avg_Success
FROM campaigns
GROUP BY Funnel_Stage
ORDER BY Avg_Success DESC;


-- ==========================================
-- 26. Customer Journey Conversion
-- ==========================================

SELECT
    Journey_Stage,
    COUNT(*) AS Users,
    SUM(
        CASE
        WHEN Converted='Yes'
        THEN 1
        ELSE 0
        END
    ) AS Converted_Users
FROM customer_journey
GROUP BY Journey_Stage;


-- ==========================================
-- 27. Device Performance
-- ==========================================

SELECT
    Device,
    COUNT(*) AS Users,
    SUM(
        CASE
        WHEN Converted='Yes'
        THEN 1
        ELSE 0
        END
    ) AS Conversions
FROM customer_journey
GROUP BY Device
ORDER BY Conversions DESC;


-- ==========================================
-- 28. High Value Customers
-- ==========================================

SELECT
    Customer_ID,
    Total_Spend,
    Loyalty_Level
FROM customers
WHERE Total_Spend >
(
SELECT AVG(Total_Spend)
FROM customers
)
ORDER BY Total_Spend DESC;


-- ==========================================
-- 29. Campaign Risk Analysis
-- ==========================================

SELECT
    Risk_Level,
    COUNT(*) AS Campaign_Count,
    AVG(Expected_ROI) AS Avg_ROI
FROM campaigns
GROUP BY Risk_Level
ORDER BY Avg_ROI DESC;


-- ==========================================
-- 30. Channel ROI Analysis
-- ==========================================

SELECT
    Marketing_Channel,
    SUM(Revenue) AS Revenue,
    SUM(Spend) AS Spend,
    ROUND(
    ((SUM(Revenue)-SUM(Spend))
    /SUM(Spend))*100,2
    ) AS ROI
FROM campaigns
GROUP BY Marketing_Channel
ORDER BY ROI DESC;