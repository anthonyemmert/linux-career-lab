
# Linux Career Lab

Hands-on Linux, PostgreSQL, and SQL practice focused on realistic fleet-management scenarios.

## Fleet SQL Project

This project uses a PostgreSQL database to practice storing, joining, filtering, and analyzing fleet data.

### Tables

- `vehicles` - vehicle information and current status
- `maintenance` - maintenance history and repair costs
- `mileage_logs` - mileage records over time
- `fuel_logs` - fuel purchases, gallons, cost, and mileage

The related tables use foreign keys connected to `vehicles.id`.

## Business Questions

### 1. Which vehicles have the highest mileage?

This query sorts vehicles by mileage so high-mileage units can be identified quickly.

Current sample result:

- TRK-001 - 91,800 miles
- VAN-002 - 76,300 miles
- VAN-003 - 62,000 miles
- VAN-001 - 48,250 miles

SQL concepts:
- `SELECT`
- `ORDER BY`

### 2. How much has been spent on maintenance for each vehicle?

Maintenance records are grouped by vehicle and their costs are added together.

Current sample result:

- TRK-001 - $650.00
- VAN-001 - $515.49
- VAN-002 - $95.00
- VAN-003 - $0.00

SQL concepts:
- `LEFT JOIN`
- `SUM`
- `GROUP BY`
- `COALESCE`


### 3. Which vehicles have no maintenance history?

A left join is used to find vehicles that do not have a matching maintenance record.

Current sample result:

- VAN-003

SQL concepts:
- `LEFT JOIN`
- `NULL`
- `WHERE`


### 4. Which vehicle has the highest total maintenance cost?

Maintenance costs are grouped by vehicle, sorted from highest to lowest, and limited to the top result.

Current sample result:

- TRK-001 - $650.00

SQL concepts:
- `INNER JOIN`
- `SUM`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`


### 5. How much fuel did each vehicle use and cost during September?

Vehicle data is joined with mileage and fuel records. Fuel gallons and costs are totaled for each vehicle while using one mileage snapshot per vehicle to avoid duplicate rows.

Current sample result:

- TRK-001 - 45.50 gallons - $168.35
- VAN-002 - 37.60 gallons - $135.35
- VAN-003 - 31.70 gallons - $113.95
- VAN-001 - 28.00 gallons - $98.00

SQL concepts:
- Multi-table joins
- Date filtering
- `SUM`
- `GROUP BY`
- `ORDER BY`


## Skills Practiced

- PostgreSQL database administration
- Primary and foreign keys
- One-to-many relationships
- `SELECT`, `WHERE`, and `ORDER BY`
- `INNER JOIN` and `LEFT JOIN`
- Aggregate functions
- `GROUP BY` and `HAVING`
- `CASE`
- Date filtering
- Multi-table joins
- Troubleshooting duplicate rows caused by joins
- Git and GitHub
- Linux command-line administration

## SQL Files

`fleet-management-queries.sql` contains the fleet-management queries used throughout the project.
