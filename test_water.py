from water import daily_demand

def test_daily_demand_value():
  assert daily_demand(5000,100) == 500000

def test_something_true():
  assert 1 == 1
