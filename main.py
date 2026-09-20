import json
import argparse
from src.funnel_engine import SalesFunnelEngine

def main():
    parser = argparse.ArgumentParser(description="Nexus Funnel Optimizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated B2B lead scoring")
    args = parser.parse_args()

    engine = SalesFunnelEngine()
    sample_lead = {
        "lead_id": "PROSPECT-881",
        "company_name": "FinScale Tech",
        "employee_count": 160,
        "uses_kubernetes": True,
        "recent_failed_deploys": 3,
        "visited_pricing_page": True
    }

    report = engine.evaluate_lead(sample_lead)
    print("="*60)
    print(" NEXUS B2B PIPELINE CONVERSION AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
