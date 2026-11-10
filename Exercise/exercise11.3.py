from employee11_3 import Employee


def test_give_default_raise():
    """Test that a default raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise()
    assert employee.annual_salary == 70_000


def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise(10_000)
    assert employee.annual_salary == 75_000