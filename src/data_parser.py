from pathlib import Path

from db_creator import create_db
import pandas as pd
from sqlalchemy.orm import Session, joinedload
from models import ENGINE, TaxiLookups, TripData


def main():
    create_db()
    time_zones_data = pd.read_csv(Path(__file__).parent.parent / "data" / "taxi_zone_lookup.csv")
    trip_data = pd.read_parquet(Path(__file__).parent.parent / "data" / "yellow_tripdata_2024-03.parquet")
    time_zones_data = time_zones_data.rename(columns={
        'LocationID': 'location_id',
        'Borough': 'borough',
        'Zone': 'zone',
    })

    trip_data = trip_data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
        'Airport_fee': 'airport_fee',
    })

    with Session(ENGINE) as session:
        try:
            last = session.query(TaxiLookups).filter(TaxiLookups.location_id == 265).first()
            if last is None:
                for _, row in time_zones_data.iterrows():
                    session.add(TaxiLookups(**row.to_dict()))
                session.commit()
                print("Data inserted successfully")
            print("Data already exists in the database")
        except Exception as e:
            print(e)

        try:
            last = session.query(TaxiLookups).filter(TripData.id == 1000000).first()
            if last is None:
                i = 0
                for _, row in trip_data.iterrows():
                    i += 1
                    session.add(TripData(**row.to_dict()))
                    if i % 1_000_000 == 0:
                        session.commit()
                        print(f"{i} rows inserted")
                session.commit()
                print(f"{i} rows inserted")
                print("Data inserted successfully")
            print("Data already exists in the database")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
