import argparse
import json
import os
from funnel.cac_ltv_engine import MarketingFunnelEngine

def main():
    parser = argparse.ArgumentParser(description="Nexus Funnel Optimizer CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample marketing acquisition cohorts")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "campaigns", "growth_funnel_cohorts.json")

    if args.demo:
        with open(data_file, "r") as f:
            cohorts = json.load(f)
        print("=== NEXUS GROWTH MARKETING & CAC/LTV AUDIT ===\n")
        for c in cohorts:
            res = MarketingFunnelEngine.calculate_unit_economics(
                spend_usd=c["spend_usd"],
                acquired_customers=c["acquired_customers"],
                arpu_monthly=c["arpu_monthly_usd"],
                gross_margin=c["gross_margin"],
                monthly_churn=c["monthly_churn_rate"]
            )
            print(f"Channel: {c['channel']} (Spend: ${c['spend_usd']:,.2f} | Acquired: {c['acquired_customers']})")
            print(f"  CAC: ${res['cac_usd']} | LTV: ${res['ltv_usd']} | LTV/CAC Ratio: {res['ltv_to_cac_ratio']}x")
            print(f"  Payback Period: {res['payback_months']} months | Rating: {res['unit_economics_rating']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
