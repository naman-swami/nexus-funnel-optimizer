# Nexus Growth Funnel & Unit Economics Optimizer

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Marketing](https://img.shields.io/badge/Domain-Growth_Marketing_Analytics-crimson.svg)](docs/saas_growth_metrics.md)
[![Standard](https://img.shields.io/badge/Metric-LTV%2FCAC_Payback-gold.svg)](docs/saas_growth_metrics.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A growth marketing and acquisition analytics platform computing customer acquisition cost (CAC), customer lifetime value (LTV), and marketing channel payback efficiency.

```
                    ┌─────────────────────────┐
                    │ Acquisition Channel Logs│
                    │ (Spend, Churn, ARPU, N) │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ funnel/cac_ltv_engine   │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  CAC & LTV Modeling │         │  Payback Period     │
      │  (LTV/CAC >= 3.0x)  │         │   (< 12 Months)     │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Channel Scaling Verdict │
                    │ (SCALE / OPTIMIZE / CUT)│
                    └─────────────────────────┘
```

## Features

- **Unit Economics Modeling**: Evaluates channel-by-channel Customer Acquisition Cost and Lifetime Value.
- **Payback Period Estimation**: Identifies months required to recover acquisition expenditure.
- **Benchmark Cohorts**: Includes multi-channel SaaS acquisition datasets.

## Directory Structure

```
nexus-funnel-optimizer/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint marketing provenance
├── funnel/
│   └── cac_ltv_engine.py            # Unit economics and payback engine
├── fixtures/
│   └── campaigns/
│       └── growth_funnel_cohorts.json # Benchmark marketing cohorts
├── docs/
│   └── saas_growth_metrics.md       # Growth benchmarks reference
├── tests/
│   └── test_agent.py                # Marketing test suite
├── optimize.py                          # Growth analytics CLI
└── requirements.txt
```

## Quick Start

```bash
# Run unit economics tests
pytest tests/ -v

# Audit sample marketing cohorts
python optimize.py --demo
```
