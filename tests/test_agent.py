import pytest
from src.funnel_engine import SalesFunnelEngine

def test_high_intent_lead():
    engine = SalesFunnelEngine()
    lead = {"lead_id": "L1", "employee_count": 200, "uses_kubernetes": True, "recent_failed_deploys": 4, "visited_pricing_page": True}
    res = engine.evaluate_lead(lead)
    assert res["qualification_tier"] == "TIER_A_IMMEDIATE_SDR"
    assert res["propensity_score"] >= 80

def test_low_intent_lead():
    engine = SalesFunnelEngine()
    lead = {"lead_id": "L2", "employee_count": 10, "uses_kubernetes": False, "recent_failed_deploys": 0, "visited_pricing_page": False}
    res = engine.evaluate_lead(lead)
    assert res["qualification_tier"] == "TIER_C_INACTIVE"
