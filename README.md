# ⚡ Tesla 5-Year TCO, FSD & Solar + Powerwall 3 Arbitrage Calculator

[![Live Interactive Calculator](https://img.shields.io/badge/Live_Web_Calculator-GitHub_Pages-f59e0b?style=for-the-badge)](https://fin-hawk-dot-com.github.io/tesla-tco-solar-calculator/)
[![Python 3.9+](https://img.shields.io/badge/CLI-Python_3.9%2B-38bdf8?style=for-the-badge)](./tesla_tco_cli.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](./LICENSE)

Open-source **5-Year EV vs. Gas Total Cost of Ownership (TCO)** and **Tesla Solar + Powerwall 3 Time-of-Use (TOU) Peak Arbitrage** calculator—available both as an **[Interactive Web App](https://fin-hawk-dot-com.github.io/tesla-tco-solar-calculator/)** and a zero-dependency Python CLI.

> **FTC & Referral Disclosure:** Ordering via our verified Tesla referral links below applies official Tesla buyer perks at checkout at zero extra cost to you:
> - 🎁 **Vehicles (Model Y / Model 3 / Cybertruck / S / X):** **[Get a free month of Full Self-Driving (Supervised) when you use this link](https://tesla.com/get-app/referral?code=justin929372)** (`code=justin929372`)
> - ☀️ **Tesla Solar & Powerwall 3:** **[Get $400 off your Tesla Solar purchase when you use this link](https://ts.la/justin929372)** (`ts.la/justin929372`)

---

## 🧮 1. Try the Live Interactive Calculator

👉 **[Launch Interactive Calculator: https://fin-hawk-dot-com.github.io/tesla-tco-solar-calculator/](https://fin-hawk-dot-com.github.io/tesla-tco-solar-calculator/)**

Adjust sliders in real time for:
- **Annual Mileage** (`5,000` – `30,000` mi/yr)
- **Home Off-Peak TOU Electricity Rate** (`$0.05` – `$0.35` / kWh, factoring in `88%` Level 2 wall-to-battery efficiency)
- **Local Gasoline Price** (`$2.25` – `$6.50` / gallon)
- **Federal ($7,500) & State/Utility EV Rebates**

---

## 📊 2. Pre-Computed 2026 5-Year TCO Benchmarks (12,000 mi/yr, $0.11/kWh Off-Peak, $3.65/gal Gas)

| Tesla Model | Base MSRP | EPA Efficiency | 5-Yr Charging vs Gas Saved | Fed Tax Credit | 5-Yr Net Effective Cost | Verified Buyer Perk |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Model 3 Long Range** | $42,490 | 250 Wh/mi | -$8,225 | -$7,500 | **$26,666** | [Free Month FSD](https://tesla.com/get-app/referral?code=justin929372) |
| **Model Y Long Range** | $44,990 | 275 Wh/mi | -$9,061 | -$7,500 | **$28,330** | [Free Month FSD](https://tesla.com/get-app/referral?code=justin929372) |
| **Cybertruck AWD** | $79,990 | 410 Wh/mi | -$11,833 | -$7,500 | **$60,558** | [Free Month FSD](https://tesla.com/get-app/referral?code=justin929372) |
| **Model S AWD** | $74,990 | 280 Wh/mi | -$10,556 | $0 | **$64,335** | [Free Month FSD](https://tesla.com/get-app/referral?code=justin929372) |
| **Model X AWD** | $79,990 | 330 Wh/mi | -$11,175 | $0 | **$68,716** | [Free Month FSD](https://tesla.com/get-app/referral?code=justin929372) |

---

## ☀️ 3. Tesla Solar + Powerwall 3 Time-of-Use (TOU) Peak Shaving Math

Utilities with steep afternoon/evening TOU tariffs (`$0.28+/kWh` peak from 4 PM–8 PM vs `$0.10/kWh` off-peak) unlock compounding arbitrage with **Powerwall 3 (`13.5 kWh` usable LFP capacity)**:

- **Gross 8.5 kW Solar + 1x Powerwall 3 System:** `~$34,025`
- **30% Federal Residential Clean Energy Credit:** `-$10,208`
- **Verified Tesla Solar Referral Discount ([ts.la/justin929372](https://ts.la/justin929372)):** `-$400`
- **Net Installed Cost:** **`$23,417`**
- **Estimated Annual Solar + TOU Arbitrage Yield:** `~$2,866/yr` (~`8.2 yr` payback, **`+$5,240` 10-year net profit**)

---

## 💻 4. Run the Python CLI Locally

```bash
git clone https://github.com/fin-hawk-dot-com/tesla-tco-solar-calculator.git
cd tesla-tco-solar-calculator
python tesla_tco_cli.py --model model-y --miles 15000 --kwh 0.11 --gas 3.75 --state-rebate 2500
```
