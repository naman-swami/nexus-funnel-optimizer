"""
Nexus Growth Marketing & Customer Unit Economics Engine
Calculates Customer Acquisition Cost (CAC), Lifetime Value (LTV), and LTV/CAC payback health.
"""
from typing import Dict, Any

class MarketingFunnelEngine:
    @staticmethod
    def calculate_unit_economics(
        spend_usd: float,
        acquired_customers: int,
        arpu_monthly: float,
        gross_margin: float,
        monthly_churn: float
    ) -> Dict[str, Any]:
        # CAC = Spend / Customers
        cac = round(spend_usd / max(1, acquired_customers), 2)

        # LTV = (ARPU * Gross Margin) / Churn
        monthly_contribution = arpu_monthly * gross_margin
        ltv = round(monthly_contribution / max(0.001, monthly_churn), 2)

        ltv_cac_ratio = round(ltv / max(1.0, cac), 2)

        # Payback period in months: CAC / monthly_contribution
        payback_months = round(cac / max(0.1, monthly_contribution), 1)

        health = "EXCELLENT_SCALABLE" if ltv_cac_ratio >= 3.0 else "ACCEPTABLE" if ltv_cac_ratio >= 1.5 else "UNSUSTAINABLE_BURN"

        return {
            "cac_usd": cac,
            "ltv_usd": ltv,
            "ltv_to_cac_ratio": ltv_cac_ratio,
            "payback_months": payback_months,
            "unit_economics_rating": health
        }
