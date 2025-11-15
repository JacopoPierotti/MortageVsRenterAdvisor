import streamlit as st

from scr.preprocess import FinancialInputs

from statistics import mean


def calculate_net_yearly_payment(
    financial_inputs: FinancialInputs,
) -> tuple[list[float], float]:
    """
    Calculates the average net monthly payment for each year of the mortgage.
    (This is the user's provided code, corrected)

    Args:
        financial_inputs: A custom object/class containing mortgage parameters.

    Returns:
        A list of average net monthly payments for each year of the mortgage term.
    """

    loan_amount = financial_inputs.mortage
    yearly_interest_rate = financial_inputs.interest_rate
    tax_rate = financial_inputs.tax_rate
    term_years = financial_inputs.mortage_years
    extra_monthly_costs = financial_inputs.extra_monthly_costs

    PAYMENTS_PER_YEAR = 12
    # This is the total number of payments (e.g., 30 * 12 = 360)
    total_payments_n = term_years * PAYMENTS_PER_YEAR

    if yearly_interest_rate == 0:
        monthly_interest_rate_i = 0
    else:
        monthly_interest_rate_i = yearly_interest_rate / PAYMENTS_PER_YEAR

    # 1. Calculate the constant Gross Monthly Payment (M)
    if monthly_interest_rate_i == 0:
        gross_monthly_payment = loan_amount / total_payments_n
    else:
        factor = (1 + monthly_interest_rate_i) ** total_payments_n
        gross_monthly_payment = (
            loan_amount * (monthly_interest_rate_i * factor) / (factor - 1)
        )

    remaining_balance = loan_amount
    monthly_net_payments = []
    yearly_net_payments = []  # This will hold the 30 average values

    # 2. Iterate through ALL months of the entire mortgage term
    #    (e.g., 1 to 360)
    for month in range(1, total_payments_n + 1):
        # Interest is calculated on the remaining balance
        interest_paid_month = remaining_balance * monthly_interest_rate_i

        # Principal (Aflossing) is the remainder of the gross payment
        principal_paid_month = gross_monthly_payment - interest_paid_month

        # Monthly Tax Deduction
        monthly_tax_deduction = interest_paid_month * tax_rate

        # Net Monthly Payment
        net_monthly_payment = gross_monthly_payment - monthly_tax_deduction

        # Add the net payment for the current month to a temporary list
        monthly_net_payments.append(round(net_monthly_payment, 2))

        # Check if we have reached the end of a year
        if len(monthly_net_payments) == 12:
            # If so, calculate the average net monthly payment for that year
            average_montly_net_payment = (
                round(mean(monthly_net_payments), 2) + extra_monthly_costs
            )
            yearly_net_payments.append(average_montly_net_payment)
            # And reset the temporary list for the next year
            monthly_net_payments = []

        # Update the balance for the next month's calculation
        remaining_balance -= principal_paid_month

    return yearly_net_payments, gross_monthly_payment


def calculate_rent_increase(financial_inputs: FinancialInputs) -> list[float]:
    """
    Calculates the rent increase over the years based on inflation.

    Args:
        financial_inputs: A custom object/class containing mortgage parameters.

    Returns:
        A list of rent amounts for each year.
    """
    rent = financial_inputs.rent
    inflation = financial_inputs.inflation
    term_years = financial_inputs.mortage_years

    yearly_rents = []

    for year in range(term_years):
        adjusted_rent = rent * ((1 + inflation) ** year)
        yearly_rents.append(round(adjusted_rent, 2))

    return yearly_rents


def calculate_house_values(financial_inputs: FinancialInputs) -> list[float]:

    house_value = financial_inputs.house_value
    yearly_appreciation = financial_inputs.yearly_house_appreciation
    term_years = financial_inputs.mortage_years
    include_overbid_in_reselling = financial_inputs.include_overbid_in_reselling
    if include_overbid_in_reselling:
        overbidding = financial_inputs.overbid_price
        house_value += overbidding

    house_values = []
    for year in range(term_years):
        adjusted_value = house_value * ((1 + yearly_appreciation) ** year)
        house_values.append(round(adjusted_value, 2))
    return house_values


def calculate_stock_values(financial_inputs: FinancialInputs) -> list[float]:
    house_value = financial_inputs.house_value
    overbid_price = financial_inputs.overbid_price
    renovation_price = financial_inputs.renovation_price
    mortage = financial_inputs.mortage

    stocks = house_value + overbid_price + renovation_price - mortage

    yearly_stocks_increase = financial_inputs.yearly_stocks_increase
    term_years = financial_inputs.mortage_years
    stock_values = []
    for year in range(term_years):
        adjusted_value = stocks * ((1 + yearly_stocks_increase) ** year)
        stock_values.append(round(adjusted_value, 2))
    return stock_values


def calculate_total_debt(
    financial_inputs: FinancialInputs, gross_monthly_payment: float
) -> list[float]:

    term_years = financial_inputs.mortage_years
    PAYMENTS_PER_YEAR = 12
    total_payments_n = term_years * PAYMENTS_PER_YEAR

    total_to_be_paid = gross_monthly_payment * total_payments_n

    yearly_remaining_debt = []
    amount_paid = 0
    for year in range(1, term_years + 1):
        amount_paid += gross_monthly_payment * PAYMENTS_PER_YEAR
        remaining_debt = total_to_be_paid - amount_paid
        yearly_remaining_debt.append(round(remaining_debt, 2))

    return yearly_remaining_debt


def calculate_remaining_principal_per_year(
    financial_inputs: FinancialInputs, gross_monthly_payment: float
) -> list[float]:

    loan_amount = financial_inputs.mortage
    interest_rate = financial_inputs.interest_rate
    term_years = financial_inputs.mortage_years

    PAYMENTS_PER_YEAR = 12
    total_payments_n = term_years * PAYMENTS_PER_YEAR

    if interest_rate == 0:
        monthly_interest_rate_i = 0
    else:
        monthly_interest_rate_i = interest_rate / PAYMENTS_PER_YEAR

    remaining_balance = loan_amount
    remaining_principal_per_year = []

    # 2. Iterate through ALL months (e.g., 360)
    for month in range(1, total_payments_n + 1):
        # Interest paid this month (on the starting balance for this month)
        interest_paid_month = remaining_balance * monthly_interest_rate_i

        # Principal (Aflossing) paid this month
        principal_paid_month = gross_monthly_payment - interest_paid_month

        # Update the remaining balance
        remaining_balance -= principal_paid_month

        # Check if it's the end of a year (every 12 months)
        if month % PAYMENTS_PER_YEAR == 0:
            # Record the balance remaining after the 12th payment of the year
            remaining_principal_per_year.append(max(0.0, round(remaining_balance, 2)))

    return remaining_principal_per_year


def compute_delta(
    financial_inputs: FinancialInputs,
    net_yearly_payments: list[float],
    yearly_rents: list[float],
    stock_values: list[float],
    house_values: list[float],
    total_debt: list[float],
) -> list[float]:

    term_years = financial_inputs.mortage_years
    overbid_price = financial_inputs.overbid_price
    overhead_costs = financial_inputs.overhead_costs
    are_you_younger_than_32 = financial_inputs.is_younger_than_32
    house_value = financial_inputs.house_value

    delta = []
    for year in range(term_years):
        value = house_values[year] + 12 * (
            net_yearly_payments[year] - yearly_rents[year]
        )
        loss = stock_values[year] + total_debt[year] + overbid_price + overhead_costs
        if not are_you_younger_than_32:
            loss += house_value * 0.02  # extra cost for younger than 32
        delta.append(round(value - loss, 2))
    return delta


def table(financial_inputs: FinancialInputs) -> None:
    net_yearly_payments, gross_monthly_payment = calculate_net_yearly_payment(
        financial_inputs
    )
    yearly_rents = calculate_rent_increase(financial_inputs)
    house_values = calculate_house_values(financial_inputs)
    stock_values = calculate_stock_values(financial_inputs)
    remaining_principal = calculate_remaining_principal_per_year(
        financial_inputs, gross_monthly_payment
    )
    delta = compute_delta(
        financial_inputs,
        net_yearly_payments,
        yearly_rents,
        stock_values,
        house_values,
        remaining_principal,
    )

    # create a streamlit table
    st.subheader("Yearly Comparison Table")
    data = {
        "Average Net Monthly Payment (Buying)": net_yearly_payments,
        "Yearly Rent": yearly_rents,
        "Estimated House Value": house_values,
        "Estimated Stock Value Loss": stock_values,
        "Total Principal Remaining": remaining_principal,
        "Delta (Buying - Renting)": delta,
    }
    st.table(data)
