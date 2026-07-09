USE ai_marketing_platform;


-- ==========================================
-- CHANNELS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/channels.csv'

INTO TABLE channels

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;



-- ==========================================
-- PRODUCTS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/products.csv'

INTO TABLE products

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;



-- ==========================================
-- LOCATIONS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/locations.csv'

INTO TABLE locations

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;

-- ==========================================
-- CUSTOMERS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/customers.csv'

INTO TABLE customers

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;



-- ==========================================
-- CAMPAIGNS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/campaigns.csv'

INTO TABLE campaigns

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;

-- ==========================================
-- TRANSACTIONS IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/transactions.csv'

INTO TABLE transactions

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;



-- ==========================================
-- CAMPAIGN PERFORMANCE IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/campaign_performance.csv'

INTO TABLE campaign_performance

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;



-- ==========================================
-- CUSTOMER JOURNEY IMPORT
-- ==========================================

LOAD DATA INFILE 'C:/Users/kartik/AI-Marketing-Campaign-Intelligence-Platform/data/raw/customer_journey.csv'

INTO TABLE customer_journey

FIELDS TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY '\n'

IGNORE 1 ROWS;