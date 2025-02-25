# Berkeley
Berkeley ML/AI Modules and Practical application II: Used Car Dealership

## Practical Application1 <Will the Customer Accept the Coupon>

## [Juypter Notebook](https://github.com/Jhonson924/berkeley/blob/main/Used_Car_Dealership/usedCarDealership.ipynb)

### Context
- Key Factors influences dealership which make Car More or Less expensive eg: Market Demand
- Consumer values in used Cars.

### Business Problem Statement

#### Consumer Vaules in Used Cars 
- Car Brand (Luxury vs General)
- Car Type (Hybrid, Electric, Fuel)
- Car Year Make, Odometer
- Car Efficiency & Features (Engines, Premium (Leather Seat, Sunroof, colors))
- Car History (No acciedent report, service , tire)
- Car Technology Features (info and entertianment)
- Car Body/Style/Capacity (SUV, Sedan, Trucks, 5 seater, 7 Seater..)
- Car Price

#### What makes Car More or Less Expensive
- Market Factors
-- Demand & Popularity
-- Availability & Supply Chain
-- Seasonal Trends
-- Competitor pricing
- Consumer Values understanding
-- Car Brand , Type , Year & Mileage
-- Car History
-- Car Body/Style/Capacity
-- Car Price

### Project Goal
- What Drives the Price of Car

### Logical Data

![Business Understading](./images/usedCarContext.png)

### Key Findings

#### Business Understanding

#### Data Understanding & Analytics
-- Check for zero Values in numerical features
-- Check for Zero values in Categoraial features
-- Check for Duplicate records
-- Check for Unique Records
-- Check for Outliers
-- Check for Missing Values (NaN)

#### Data Preparation , PCA for removing outliers , Data encoding
-- Drop row for duplicate VIN number based on price and odometer
-- Drop rows for VIN column = '0'
-- Drop Columns that are not required (id, VIN & region)
-- Drop Columns for size contains 71% of missing value
-- Drop zero values for Price & Odometer
-- Fill categorial Null values (NaN) to Not specified
-- Drop null values for numerical field
-- Convert DataTypes Object to String
-- Log Transformation for outliers
-- Applying PCA for removing outliers
-- Data Encoding
-- Ordinal encoding
-- One hot encoding for fuel
