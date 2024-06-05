from models import (
    TaxiLookups,
    TripData,
    Base,
    ENGINE,
)


def create_db():
    Base.metadata.create_all(ENGINE)
