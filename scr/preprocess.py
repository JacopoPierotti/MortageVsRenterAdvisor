import streamlit as st

from scr.constants import (
    HOUSE_VALUE_DEFAULT,
    EXTRA_MONTHLY_COSTS_DEFAULT,
    MONTHLY_RENT_DEFAULT,
    OVERBID_DEFAULT,
    RENNOVATION_PRICE_DEFAULT,
    YEARLY_HOUSE_APPRECIATION_DEFAULT,
    YEARLY_STOCK_INCREASE_DEFAULT,
    YOUNGER_THAN_32_DEFAULT,
)


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
        house_value = st.number_input(
            "House Value",
            min_value=0,
            step=10000,
            key="house_value",
            value=HOUSE_VALUE_DEFAULT,
        )
        is_younger_than_32 = st.checkbox(
            "Are you younger than 32 y.o.?",
            key="is_younger_than_32",
            value=YOUNGER_THAN_32_DEFAULT,
        )

    with col2:
        extra_monthly_costs = st.number_input(
            "Extra Monthly Costs (e.g., erfpacht)",
            min_value=0,
            step=50,
            key="extra_monthly_costs",
            value=EXTRA_MONTHLY_COSTS_DEFAULT,
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

    with col3:
        yearly_house_appreciation = st.number_input(
            "Yearly House Appreciation (%)",
            min_value=0.0,
            step=0.5,
            format="%.2f",
            key="yearly_house_appreciation",
            value=YEARLY_HOUSE_APPRECIATION_DEFAULT,
        )
        yearly_stocks_increase = st.number_input(
            "Yearly Stocks Increase (%)",
            min_value=0.0,
            step=0.5,
            format="%.2f",
            key="yearly_stocks_increase",
            value=YEARLY_STOCK_INCREASE_DEFAULT,
        )

    return {
        "rent": rent,
        "house_value": house_value,
        "is_younger_than_32": is_younger_than_32,
        "extra_monthly_costs": extra_monthly_costs,
        "overbid_price": overbid_price,
        "renovation_price": renovation_price,
        "yearly_house_appreciation": yearly_house_appreciation,
        "yearly_stocks_increase": yearly_stocks_increase,
    }
