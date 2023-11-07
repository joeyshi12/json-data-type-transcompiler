import datetime
from dataclasses import dataclass

@dataclass
class Root:
    employees: list[employeesItem]

@dataclass
class employeesItem:
    firstName: str
    lastName: str
