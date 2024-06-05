from datetime import datetime, timezone

from sqlalchemy import (
    FLOAT,
    INTEGER,
    TIMESTAMP,
    Column,
    ForeignKey,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base

from settings import settings

Base = declarative_base()
ENGINE = create_engine(settings.PG_DSN)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TaxiLookups(Base):
    __tablename__: str = "taxi_lookups"
    location_id: int = Column(  # type: ignore
        "LocationID",
        INTEGER,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )
    borough: str = Column("Borough", String, nullable=False)
    zone: str = Column("Zone", String, nullable=False)
    service_zone: str = Column("service_zone", String, nullable=False)


class TripData(Base):
    __tablename__: str = "trip_data"
    id: int = Column(  # type: ignore
        "id",
        INTEGER,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )
    vendor_id: int = Column(  # type: ignore
        "VendorID",
        INTEGER,
    )
    tpep_pickup_datetime: datetime = Column("tpep_pickup_datetime", TIMESTAMP)
    tpep_dropoff_datetime: datetime = Column("tpep_dropoff_datetime", TIMESTAMP)
    passenger_count: float = Column("passenger_count", FLOAT)
    trip_distance: float = Column("trip_distance", FLOAT)
    ratecode_id: float = Column("RatecodeID", FLOAT)
    store_and_fwd_flag: str = Column("store_and_fwd_flag", String)
    pu_location_id: int = Column("PULocationID", ForeignKey("taxi_lookups.LocationID"))
    do_location_id: int = Column("DOLocationID", ForeignKey("taxi_lookups.LocationID"))
    payment_type: int = Column("payment_type", INTEGER)
    fare_amount: float = Column("fare_amount", FLOAT)
    extra: float = Column("extra", FLOAT)
    mta_tax: float = Column("mta_tax", FLOAT)
    tip_amount: float = Column("tip_amount", FLOAT)
    tolls_amount: float = Column("tolls_amount", FLOAT)
    improvement_surcharge: float = Column("improvement_surcharge", FLOAT)
    total_amount: float = Column("total_amount", FLOAT)
    congestion_surcharge: float = Column("congestion_surcharge", FLOAT)
    airport_fee: float = Column("Airport_fee", FLOAT)
