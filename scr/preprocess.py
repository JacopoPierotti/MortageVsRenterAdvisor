import streamlit as st
from dataclasses import dataclass

from scr.constants import (
    HOUSE_VALUE_DEFAULT,
    EXTRA_MONTHLY_COSTS_DEFAULT,
    MONTHLY_RENT_DEFAULT,
    OVERBID_DEFAULT,
    RENNOVATION_PRICE_DEFAULT,
    YEARLY_HOUSE_APPRECIATION_DEFAULT,
    YEARLY_STOCK_INCREASE_DEFAULT,
    YOUNGER_THAN_32_DEFAULT,
    MORTAGE_DEFAULT,
    INFLATION_DEFAULT,
    INTEREST_RATE_DEFAULT,
    FLOAT_STEP,
    FLOAT_FORMAT,
    TAX_RATE_DEFAULT,
    OVERHEAD_COSTS_DEFAULT,
)


@dataclass
class FinancialInputs:
    rent: float
    inflation: float
    house_value: float
    is_younger_than_32: bool
    extra_monthly_costs: float
    overbid_price: float
    renovation_price: float
    yearly_house_appreciation: float
    yearly_stocks_increase: float
    mortage: float
    interest_rate: float
    mortage_years: int
    tax_rate: float
    overhead_costs: float
    include_overbid_in_reselling: bool


def preprocess():
    """
    Creates a Streamlit interface with three columns to gather user inputs for financial calculations.

    The inputs include rent, house value, age, extra costs, overbid price, renovation price,
    and appreciation percentages for house and stocks.

    Returns:
        dict: A dictionary containing all the user-provided values.
    """
    st.header("Financial Inputs")
    col1, col2, col3 = st.columns(3)

    with col1:
        rent = st.number_input(
            "Monthly Rent",
            min_value=0,
            step=100,
            key="rent",
            value=MONTHLY_RENT_DEFAULT,
        )
        inflation = st.number_input(
            "Rent Inflation",
            min_value=0.0,
            step=FLOAT_STEP,
            format=FLOAT_FORMAT,
            key="inflation",
            value=INFLATION_DEFAULT,
        )
        is_younger_than_32 = st.checkbox(
            "Are you younger than 32 y.o.?",
            key="is_younger_than_32",
            value=YOUNGER_THAN_32_DEFAULT,
        )
        mortage_years = st.selectbox(
            "Mortgage Term (years)",
            options=[10, 15, 20, 25, 30],
            key="mortage_years",
            index=4,
        )
        overhead_costs = st.number_input(
            "Overhead Costs (notary, etc etc)",
            min_value=0,
            step=1,
            key="overhead_costs",
            value=OVERHEAD_COSTS_DEFAULT,
        )

    with col2:
        house_value = st.number_input(
            "House Value",
            min_value=0,
            step=10000,
            key="house_value",
            value=HOUSE_VALUE_DEFAULT,
        )
        overbid_price = st.number_input(
            "Overbid Price",
            min_value=0,
            step=1000,
            key="overbid_price",
            value=OVERBID_DEFAULT,
        )
        renovation_price = st.number_input(
            "Renovation Price",
            min_value=0,
            step=1000,
            key="renovation_price",
            value=RENNOVATION_PRICE_DEFAULT,
        )
        mortage = st.number_input(
            "Bank Mortage",
            min_value=0,
            step=1000,
            key="mortage",
            value=MORTAGE_DEFAULT,
        )
        include_overbid_in_reselling = st.checkbox(
            "Include Overbid Price in Reselling Calculation?",
            key="include_overbid_in_reselling",
            value=False,
        )

    with col3:
        extra_monthly_costs = st.number_input(
            "Extra Monthly Costs (e.g., erfpacht)",
            min_value=0,
            step=50,
            key="extra_monthly_costs",
            value=EXTRA_MONTHLY_COSTS_DEFAULT,
        )
        interest_rate = st.number_input(
            "Bank Interest Rate (%)",
            min_value=0.0,
            step=FLOAT_STEP,
            format=FLOAT_FORMAT,
            key="interest_rate",
            value=INTEREST_RATE_DEFAULT,
        )
        yearly_house_appreciation = st.number_input(
            "Yearly House Appreciation (%)",
            min_value=0.0,
            step=FLOAT_STEP,
            format=FLOAT_FORMAT,
            key="yearly_house_appreciation",
            value=YEARLY_HOUSE_APPRECIATION_DEFAULT,
        )
        yearly_stocks_increase = st.number_input(
            "Yearly Stocks Increase (%)",
            min_value=0.0,
            step=FLOAT_STEP,
            format=FLOAT_FORMAT,
            key="yearly_stocks_increase",
            value=YEARLY_STOCK_INCREASE_DEFAULT,
        )
        tax_rate = st.number_input(
            "Tax Rate (%)",
            min_value=0.0,
            step=FLOAT_STEP,
            format=FLOAT_FORMAT,
            key="tax_rate",
            value=TAX_RATE_DEFAULT,
        )

    financial_inputs = FinancialInputs(
        rent=rent,
        inflation=inflation,
        house_value=house_value,
        is_younger_than_32=is_younger_than_32,
        extra_monthly_costs=extra_monthly_costs,
        overbid_price=overbid_price,
        renovation_price=renovation_price,
        yearly_house_appreciation=yearly_house_appreciation,
        yearly_stocks_increase=yearly_stocks_increase,
        mortage=mortage,
        interest_rate=interest_rate,
        mortage_years=mortage_years,
        tax_rate=tax_rate,
        overhead_costs=overhead_costs,
        include_overbid_in_reselling=include_overbid_in_reselling,
    )

    return financial_inputs
