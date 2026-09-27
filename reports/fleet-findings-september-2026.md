# Fleet Maintenance and Downtime Analysis

September 2026 | SQL Portfolio Project

## Project Overview

This project analyzes sample fleet maintenance records
using PostgreSQL. The goal is to identify maintenance
spending patterns, repair frequency, and vehicle downtime.

The dataset contains four vehicles with maintenance
and downtime records from July through September 2026.

## Fleet Summary

| Metric | Result |
|---|---:|
| Vehicles | 4 |
| Maintenance records | 4 |
| Total maintenance cost | $1,260.49 |
| Total downtime | 6 days |

## Vehicle Performance

| Vehicle | Records | Cost | Downtime |
|---|---:|---:|---:|
| TRK-001 | 1 | $650.00 | 3 days |
| VAN-001 | 2 | $515.49 | 2 days |
| VAN-002 | 1 | $95.00 | 1 day |
| VAN-003 | 0 | $0.00 | 0 days |

## Key Findings

1. TRK-001 accounts for the highest recorded
   maintenance spending at $650 and has the
   most downtime at three elapsed days.

2. VAN-001 has the highest number of maintenance
   records, with two services totaling $515.49.

3. VAN-003 has no recorded maintenance or downtime
   in the available dataset.

## Recommendations

- Review TRK-001's maintenance history and monitor
  future repair costs and downtime.

- Track maintenance costs and service frequency
  together to identify developing trends.

- Confirm maintenance-record completeness before
  interpreting missing records as no maintenance.

## Methodology

Data was stored and analyzed using PostgreSQL.

CTEs summarized maintenance costs, record counts,
and downtime separately to prevent duplicate totals
when joining multiple tables.

Results were exported to CSV and validated using
Linux AWK.

This project uses synthetic sample data. Downtime
represents elapsed days, not necessarily full days
of operational unavailability. Findings are
illustrative rather than representative of a real fleet.
