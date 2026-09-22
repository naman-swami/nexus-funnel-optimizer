# Nexus B2B Growth Funnel & Unit Economics Engine

> **SaaS Marketing Funnel Attribution, Cohort Churn, and Unit Economics Oracle**  
> Operationalizing Customer Acquisition Cost (CAC), Lifetime Value (LTV), and Payback Periods.

---

### SaaS Unit Economics Formulations

#### 1. Customer Acquisition Cost (CAC)
$$\text{CAC} = \frac{\sum \text{Sales \& Marketing Expenses}}{\text{New Customers Acquired}}$$

#### 2. Customer Lifetime Value (LTV)
$$\text{LTV} = \frac{\text{Average Revenue Per Account (ARPA)} \times \text{Gross Margin (\%)}}{\text{Monthly Logo Churn Rate (\%)}}$$

#### 3. Healthy Growth Benchmarks
- **LTV / CAC Ratio**: Target $\ge 3.0\times$ (Below $1.0\times$ indicates unsustainable acquisition).
- **CAC Payback Period**: Target $\le 12\text{ months}$ (Calculated as $\frac{\text{CAC}}{\text{ARPA} \times \text{Gross Margin}}$).

---

### Funnel Stage Conversion Waterfall

Evaluated across benchmark growth cohorts (`fixtures/campaigns/growth_funnel_cohorts.json`):

```
[100,000 Visitors] ──► 4.2% Conv ──► [4,200 MQLs]
                                            │
                                            ▼ 28.5% Conv
                                      [1,197 SQLs]
                                            │
                                            ▼ 45.0% Conv
                                      [538 Opportunities]
                                            │
                                            ▼ 22.3% Conv
                                      [120 Closed Won Customers]
```

**Cohort Financial Verdict:**
- Total Pipeline Spend: $\$180,000.00$
- Blended CAC: $\$1,500.00$ | Customer LTV: $\$7,200.00$ | **LTV/CAC: $4.8	imes$**
- Payback Period: **7.5 months** (Status: **PRIME EFFICIENCY**)

---

### Funnel Analytics CLI

```bash
# Run unit economics optimization simulation
python optimize.py --demo

# Verify financial attribution test suite
pytest tests/ -v
```

Financial definitions, cohort accounting rubrics, and payback thresholds are documented in [UNIT_ECONOMICS_RUBRIC.md](UNIT_ECONOMICS_RUBRIC.md).
