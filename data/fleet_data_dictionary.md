# Fleet Analytics Data Dictionary

## Dataset Overview

The fleet analytics dataset is a synthetic 75-vehicle dataset created for practicing fleet data analysis, reporting, and Power BI.

File: `fleet_analytics.csv`

The dataset includes vehicle information, mileage, maintenance activity, downtime, fuel usage, and calculated operating-cost metrics.

| Field | Data Type | Description |
|---|---|---|
| vehicle_number | Text | Unique identifier assigned to each fleet vehicle |
| year | Integer | Vehicle model year |
| vehicle_age | Integer | Vehicle age calculated as 2026 minus model year |
| make | Text | Vehicle manufacturer |
| model | Text | Vehicle model |
| vehicle_type | Text | Vehicle category such as Van, Pickup, or Truck |
| mileage | Integer | Current vehicle mileage |
| status | Text | Current fleet status: Active, Maintenance, or Out of Service |
| maintenance_cost | Decimal | Total maintenance and repair cost in the sample reporting period |
| repair_count | Integer | Number of maintenance or repair events |
| downtime_days | Integer | Number of days the vehicle was unavailable |
| fuel_gallons | Decimal | Fuel consumed during the sample reporting period |
| fuel_cost | Decimal | Total fuel cost |
| total_operating_cost | Decimal | Maintenance cost plus fuel cost |
| cost_per_mile | Decimal | Simplified cost-to-mile ratio calculated using total operating cost and current vehicle mileage |

## Calculated Fields

### Vehicle Age

Vehicle age is calculated from the vehicle model year:

2026 - year

### Total Operating Cost

Total operating cost combines maintenance and fuel expenses:

maintenance_cost + fuel_cost

### Cost Per Mile

This project uses a simplified cost-to-mile ratio to compare operating cost relative to each vehicle's current mileage:

total_operating_cost / mileage

Because the operating-cost values represent a sample reporting period while mileage represents current vehicle mileage, this metric should be treated as a comparative portfolio metric rather than a true period cost-per-mile calculation.

## Data Notes

- The dataset contains 75 unique vehicles.
- Vehicle numbers contain no duplicates.
- No fields contain missing values.
- The data is synthetic and is intended for training and portfolio demonstration.
- Values should not be interpreted as actual company fleet performance.
