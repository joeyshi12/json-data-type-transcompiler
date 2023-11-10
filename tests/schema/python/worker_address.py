import datetime
from dataclasses import dataclass

@dataclass
class Root:
    AddressId: int
    EffectiveStartDate: str
    EffectiveEndDate: str
    AddressLine1: str
    AddressLine2: AddressLine2
    AddressLine3: AddressLine3
    AddressLine4: AddressLine4
    TownOrCity: str
    Region1: Region1
    Region2: Region2
    Region3: Region3
    Country: str
    PostalCode: PostalCode
    LongPostalCode: LongPostalCode
    AddlAddressAttribute1: AddlAddressAttribute1
    AddlAddressAttribute2: AddlAddressAttribute2
    AddlAddressAttribute3: AddlAddressAttribute3
    AddlAddressAttribute4: AddlAddressAttribute4
    AddlAddressAttribute5: AddlAddressAttribute5
    CreatedBy: str
    CreationDate: str
    LastUpdatedBy: str
    LastUpdateDate: str
    PersonAddrUsageId: int
    AddressType: str
    PrimaryFlag: bool
