import os
import pytest
from funnel.cac_ltv_engine import MarketingFunnelEngine

def test_unit_economics_calculation():
    res = MarketingFunnelEngine.calculate_unit_economics(
        spend_usd=10000.0, acquired_customers=100, arpu_monthly=100.0, gross_margin=0.80, monthly_churn=0.02
    )
    # CAC = 10000 / 100 = 100.0
    # LTV = (100 * 0.8) / 0.02 = 80 / 0.02 = 4000.0
    assert res["cac_usd"] == 100.0
    assert res["ltv_usd"] == 4000.0
    assert res["ltv_to_cac_ratio"] == 40.0
    assert res["unit_economics_rating"] == "EXCELLENT_SCALABLE"
