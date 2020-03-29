import pytest
from app import data

def test_employees():
    employees = data.get_employees()
    print(employees)
