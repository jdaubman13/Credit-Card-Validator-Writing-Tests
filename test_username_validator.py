import pytest


class CreditCardValidator:
    """Test suite for credit_card_validator function"""

    # ===== POSITIVE CASES (should return True) =====
    
    def test_visa_starts_with_four(self):
        "Tests that a visa card that starts with 4 works"
        assert CreditCardValidator(4111111111111111) == True

    def test_visa_has_sixteen_digit(self):
        "Tests that a visa card with 16 digits works"
        assert CreditCardValidator(4539578763621486) == True

    def test_mastercard_middlerange1(self):
        "Tests a middle number of the 51-55 mastercard starting range works"
        assert CreditCardValidator(5424180279791732) == True

    def test_mastercard_middlerange2(self):
        "Tests a middle number of the 2221-2720 mastercard starting range works"
        assert CreditCardValidator(2223003122003222) == True

    def test_mastercard_has_sixteen_digit(self);
        "Tests if a mastercard has with 16 digits works"
        assert CreditCardValidator(5105105105105100) == True

    def test_amex_starting1(self):
        "Tests if an Amex starting with 34 works"
        assert CreditCardValidator(340000000000009) == True

    def test_amex_starting1(self):
        "Tests if an Amex start with 37 works"
        assert CreditCardValidator(378734493671000) == True

    def test_amex_15(self):
        "Tests that an amex with 15 characters works"
        assert CreditCardValidator(378282246310005) == True



    # ===== NEGATIVE CASES (should return False) =====

    def test_visa_not_start_with_4(self):
        "Tests if a visa card that does not start with 4 does not work"
        assert CreditCardValidator(8279555660054222) == False

    def test_visa_not_has_sixteen_digit(self):
        "Tests if a visa card that does not have 16 digits does not work"
        assert CreditCardValidator(400005665566555) == False

    def test_mastercard_range1_bottom(self):
        "Tests the bottom outer number of the mastercard 51-55 range does not work"
        assert CreditCardValidator(5012345678901230) == False

    def test_mastercard_range1_top(self):
        "Tests the top outer number of the mastercard 51-55 range does not work"
        assert CreditCardValidator(5612345678901237) == False

    def test_mastercard_range2_bottom(self):
        "Tests the bottom outer number of the mastercard 2221-2720 range does not work"
        assert CreditCardValidator(2220123456789015) == False

    def test_mastercard_range2_top(self):
        "Tests the bottom outer number of the mastercard 2221-2720 range does not work"
        assert CreditCardValidator(2721123456789019) == False

    def test_amex_not_starting(self):
        "Tests that an Amex not starting with 34 or 37 does not work"
        assert CreditCardValidator(959827716138430) == False

    def test_amex_not_15(self):
        "Tests that an Amex without 15 characters does not work"
        assert CreditCardValidator(3712345678901234) == False

    def test_empty_input(self):
        "Ensures empty inputs do not work"
        assert CreditCardValidator() == False

    def test_luhn_failing_16(self):
        "Make sure 16 digit numbers that fail the luhn do not work"
        assert CreditCardValidator(1234567891011121)

    def test_luhn_failing_15(self):
        "Make sure 15 digit numbers that fail the luhn do not work"
        assert CreditCardValidator(123456789101112)

