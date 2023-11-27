from fake_data_app.sensor import VisitSensor
from datetime import date


def test_monday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2023, 9, 11))


def test_tuesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2023, 9, 12))


def test_wednesday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2023, 9, 13))


def test_thursday_open():
    visit_sensor = VisitSensor(1200, 300)
    assert -1 != visit_sensor.simulate_visit_count(date(2023, 9, 14))

test_thursday_open()
test_wednesday_open()
