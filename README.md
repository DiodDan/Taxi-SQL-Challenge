# This is project for UE assignment Taxi SQL challenge

### For creating and filling database with data run you have to install all dependecies in pyproject.toml and run:
```bash
python3 src/data_paser.py
```

### After that we can start to work with database.


# Homework tasks:

1. How many taxi trips were there on March 15? Consider only trips that started on March 15.
    ```sql
        SELECT 
            COUNT(id) FROM trip_data
        WHERE
            tpep_pickup_datetime >= timestamp '2024-03-15 00:00:00' AND
            tpep_pickup_datetime <= timestamp '2024-03-15 23:59:59'
    ```
    ### Explanation: We are counting all trips that started on March 15.
    ### Answer should be `128813`
2. Find the largest tip for each day. On which day it was the largest tip in March? Use the pick up time for your calculations.
    ```sql
        SELECT
            DATE(tpep_pickup_datetime) as date,
            MAX(tip_amount) as max_tip
        FROM trip_data
        GROUP BY date
        ORDER BY max_tip DESC
        LIMIT 1
    ```
    ### Explanation: We are grouping all trips by date and then we are selecting the largest tip for each day. After that we are ordering by tip amount and selecting the first row.
    ### Answer should be `2024-03-03` with `tip_amount` of `999.99`
3. What was the most popular destination for passengers picked up in central park on March 14? Use the pick up time for your calculations.
    ```sql
    SELECT
         trip_data."DOLocationID",
         COUNT(trip_data."DOLocationID") as trips_count,
         tl."Zone" as zone
    FROM
        trip_data
    JOIN 
        taxi_lookups tl on trip_data."DOLocationID" = tl."LocationID"
    WHERE
        trip_data."PULocationID" = 43 AND
        tpep_pickup_datetime >= timestamp '2024-03-14 00:00:00' AND
        tpep_pickup_datetime <= timestamp '2024-03-14 23:59:59'
    GROUP BY 
        trip_data."DOLocationID", tl."Zone"
    ORDER BY 
        trips_count DESC
    LIMIT 1
    ```
    ### Explanation: We are selecting all trips that started in Central Park on March 14. After that we are grouping all trips by dropoff location and counting them. Then we are ordering by count and selecting the first row.
    ### Answer should be `Midtown Center` with `count` of `183`
4. What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)? Enter two zone names separated by a slash For example: Jamaica Bay/Clinton East
    ```sql
        SELECT
            trip_data."PULocationID",
            trip_data."DOLocationID",
            AVG(trip_data."total_amount") as avg_amount,
            pl."Zone" as pickup_zone,
            dl."Zone" as dropoff_zone
        FROM
            trip_data
        JOIN
            taxi_lookups pl on trip_data."PULocationID" = pl."LocationID"
        JOIN
            taxi_lookups dl on trip_data."DOLocationID" = dl."LocationID"
        GROUP BY
            trip_data."PULocationID", trip_data."DOLocationID", pl."Zone", dl."Zone"
        ORDER BY
            avg_amount DESC
        LIMIT 1
    ```
    ### Explanation: We are joining trip_data with taxi_lookups twice to get zone names for pickup and dropoff locations. After that we are grouping all trips by pickup and dropoff location and calculating average total amount. Then we are ordering by average amount and selecting the first row.
    ### Answer should be `Bayside`/`Outside of NYC` with `avg_amount` of `455.05999999999995`