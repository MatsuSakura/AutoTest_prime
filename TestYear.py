import pytest

def year_month(year, month):
    if month > 12 or month < 0:
        return -1
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    if month in(4,6,9,11):
        return 30
    else:
        return 31

class Test():
    @pytest.fixture(autouse=True)
    def setUp(self):
        print("test start")
        yield
        print("test end")

    @pytest.mark.parametrize("year,month", [(1999,-1)])
    def test_skip(self, year, month):
        result = year_month(year, month)
        assert result == 31

    @pytest.mark.parametrize("year,month",[(2022,1),(2022,2),(2020,2),(2022,10)])
    def test_Days(self,year,month):
        result = year_month(year,month)
        assert result == 31

    @pytest.mark.parametrize("year,month", [(2022,2),(2020,2)])
    def test_run(self,year,month):
        result = year_month(year,month)
        assert result == 28


if __name__ == '__main__':
    pytest.main(["-s","TestYear.py"])
