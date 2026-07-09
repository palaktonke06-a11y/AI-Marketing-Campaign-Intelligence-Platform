CREATE DATABASE IF NOT EXISTS ai_marketing_platform;

USE ai_marketing_platform;

-- ==========================================
-- CHANNELS
-- ==========================================

CREATE TABLE channels (

    Channel_ID INT PRIMARY KEY,

    Channel_Name VARCHAR(100),

    Channel_Type VARCHAR(50),

    Platform VARCHAR(100),

    Cost_Model VARCHAR(50),

    Average_CTR DECIMAL(5,2),

    Average_CPC DECIMAL(10,2),

    Average_CPM DECIMAL(10,2)

);

-- ==========================================
-- PRODUCTS
-- ==========================================

CREATE TABLE products (

    Product_ID INT PRIMARY KEY,

    Product_Name VARCHAR(200),

    Category VARCHAR(100),

    Brand VARCHAR(100),

    Price DECIMAL(12,2),

    Cost DECIMAL(12,2),

    Profit_Margin DECIMAL(5,2),

    Rating DECIMAL(3,2),

    Stock INT,

    Launch_Date DATE

);

-- ==========================================
-- LOCATIONS
-- ==========================================

CREATE TABLE locations (

    Location_ID INT PRIMARY KEY,

    City VARCHAR(100),

    State VARCHAR(100),

    Region VARCHAR(100),

    Country VARCHAR(100),

    Pincode VARCHAR(20)

);

-- ==========================================
-- CUSTOMERS
-- ==========================================

CREATE TABLE customers (

    Customer_ID INT PRIMARY KEY,

    First_Name VARCHAR(100),

    Last_Name VARCHAR(100),

    Gender VARCHAR(20),

    Age INT,

    Age_Group VARCHAR(20),

    Email VARCHAR(150),

    Phone VARCHAR(30),

    Location_ID INT,

    Occupation VARCHAR(100),

    Income_Level VARCHAR(50),

    Device_Type VARCHAR(50),

    Customer_Segment VARCHAR(50),

    Loyalty_Level VARCHAR(50),

    Preferred_Channel VARCHAR(100),

    Registration_Date DATE,

    Is_Active VARCHAR(10),

    Total_Orders INT,

    Total_Spend DECIMAL(15,2),

    FOREIGN KEY (Location_ID)
        REFERENCES locations(Location_ID)

);

-- ==========================================
-- CAMPAIGNS
-- ==========================================

CREATE TABLE campaigns (

    Campaign_ID INT PRIMARY KEY,

    Campaign_Name VARCHAR(200),

    Campaign_Type VARCHAR(100),

    Campaign_Objective VARCHAR(100),

    Product_ID INT,

    Marketing_Channel VARCHAR(100),

    Industry VARCHAR(100),

    Target_Audience VARCHAR(100),

    Funnel_Stage VARCHAR(50),

    Creative_Type VARCHAR(100),

    Device_Target VARCHAR(100),

    Region_Target VARCHAR(100),

    Bid_Strategy VARCHAR(100),

    Budget DECIMAL(15,2),

    Budget_Category VARCHAR(50),

    Campaign_Duration INT,

    Start_Date DATE,

    End_Date DATE,

    Campaign_Status VARCHAR(50),

    AI_Campaign_Score DECIMAL(5,2),

    Success_Probability DECIMAL(5,2),

    Risk_Level VARCHAR(50),

    Priority VARCHAR(50),

    Expected_ROI DECIMAL(10,2),

    Estimated_Revenue DECIMAL(15,2),

    Expected_Conversions INT,

    Target_CPA DECIMAL(10,2),

    Target_ROAS DECIMAL(10,2),

    Audience_Size INT,

    Optimization_Score INT,

    Impressions BIGINT,

    CTR DECIMAL(5,2),

    Clicks BIGINT,

    Conversion_Rate DECIMAL(5,2),

    Conversions INT,

    CPC DECIMAL(10,2),

    CPM DECIMAL(10,2),

    Spend DECIMAL(15,2),

    Revenue DECIMAL(15,2),

    FOREIGN KEY (Product_ID)
        REFERENCES products(Product_ID)

);

-- ==========================================
-- TRANSACTIONS
-- ==========================================

CREATE TABLE transactions (

    Transaction_ID INT PRIMARY KEY,

    Customer_ID INT,

    Campaign_ID INT,

    Product_ID INT,

    Transaction_Date DATE,

    Quantity INT,

    Unit_Price DECIMAL(12,2),

    Gross_Amount DECIMAL(15,2),

    Discount_Percentage DECIMAL(5,2),

    Discount_Amount DECIMAL(12,2),

    Net_Amount DECIMAL(15,2),

    Coupon_Code VARCHAR(50),

    Payment_Method VARCHAR(50),

    Order_Status VARCHAR(50),

    FOREIGN KEY (Customer_ID)
        REFERENCES customers(Customer_ID),

    FOREIGN KEY (Campaign_ID)
        REFERENCES campaigns(Campaign_ID),

    FOREIGN KEY (Product_ID)
        REFERENCES products(Product_ID)

);

-- ==========================================
-- CAMPAIGN PERFORMANCE
-- ==========================================

CREATE TABLE campaign_performance (

    Performance_ID INT PRIMARY KEY,

    Campaign_ID INT,

    Performance_Date DATE,

    Impressions BIGINT,

    Clicks BIGINT,

    CTR DECIMAL(5,2),

    Conversions INT,

    Conversion_Rate DECIMAL(5,2),

    Spend DECIMAL(15,2),

    Revenue DECIMAL(15,2),

    ROI DECIMAL(10,2),

    CPC DECIMAL(10,2),

    CPM DECIMAL(10,2),

    FOREIGN KEY (Campaign_ID)
        REFERENCES campaigns(Campaign_ID)

);

-- ==========================================
-- CUSTOMER JOURNEY
-- ==========================================

CREATE TABLE customer_journey (

    Journey_ID INT PRIMARY KEY,

    Customer_ID INT,

    Campaign_ID INT,

    Journey_Date DATE,

    Journey_Stage VARCHAR(50),

    Device VARCHAR(50),

    Pages_Visited INT,

    Session_Duration INT,

    Bounce VARCHAR(10),

    Converted VARCHAR(10),

    FOREIGN KEY (Customer_ID)
        REFERENCES customers(Customer_ID),

    FOREIGN KEY (Campaign_ID)
        REFERENCES campaigns(Campaign_ID)

);