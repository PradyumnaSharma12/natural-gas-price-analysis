from gas_price_estimator import estimate_gas_price


def price_storage_contract(
    injection_date,
    withdrawal_date,
    quantity_mmbtu,
    storage_months,
    monthly_storage_cost,
    injection_cost_per_mmbtu,
    withdrawal_cost_per_mmbtu,
    transport_cost_per_trip,
):
    """
    Returns the value of a natural gas storage contract
    """

    # Prices
    buy_price = estimate_gas_price(injection_date)
    sell_price = estimate_gas_price(withdrawal_date)

    # Gross profit
    gross_profit = (sell_price - buy_price) * quantity_mmbtu

    # Costs
    storage_cost = storage_months * monthly_storage_cost
    injection_cost = injection_cost_per_mmbtu * quantity_mmbtu
    withdrawal_cost = withdrawal_cost_per_mmbtu * quantity_mmbtu
    transport_cost = 2 * transport_cost_per_trip

    # Final contract value
    contract_value = (
        gross_profit - storage_cost - injection_cost - withdrawal_cost - transport_cost
    )

    return contract_value
