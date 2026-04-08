import re

def test_email_validation():
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    assert re.match(regex, "test@example.com")
    assert re.match(regex, "user.name@domain.co.uk")
    assert not re.match(regex, "invalid-email")
    assert not re.match(regex, "test@example")
    assert not re.match(regex, "@example.com")
    print("Email validation tests passed!")

def test_revenue_calculation():
    bookings = [
        {'total': 440, 'status': 'Pending'},
        {'total': 285, 'status': 'Pending'},
        {'total': 180, 'status': 'Reserved'},
        {'total': 170, 'status': 'Confirmed'},
        {'total': 300, 'status': 'Confirmed'}
    ]
    confirmed = [b for b in bookings if b['status'] == 'Confirmed']
    revenue = sum(b['total'] for b in confirmed)
    assert revenue == 470
    print("Revenue calculation logic passed!")

if __name__ == "__main__":
    test_email_validation()
    test_revenue_calculation()
