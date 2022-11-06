import pytest

@pytest.fixture(params=[-1,0,3,5])
def data(request):
    return request.param

class TestPrime():
    def prime(self, number):
        if number < 0 or number in (0, 1):
            return False
        for element in range(2, number):
            if number % element == 0:
                return False
        return True

    @pytest.fixture(autouse=True)
    def setUp(self):
        print("test start")
        yield
        print("test end")

    def test_prime(self,data):
        result = self.prime(data)
        assert result==True

if __name__ == '__main__':
    pytest.main(["-s","TestPrime.py"])
