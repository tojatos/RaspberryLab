import pytest
from app import data

def test_employees():
    employees = data.get_employees()
    print("Employees:", employees)

def test_cards():
    cards = data.get_cards()
    print("Cards:", cards)

def test_card_readings():
    card_readings = data.get_card_readings()
    print("Card readings:", card_readings)

def test_terminals():
    terminals = data.get_terminals()
    print("Terminals:", terminals)
