from sales import calculate

def test(a,b):
    c = calculate(a,b)

    test_c = a+b

    assert c == test_c


test(1,25)
test(101,12)
test(40,1)