#!/usr/bin/env python3
"""
Zero-dependency CLI calculator for Tesla 5-Year EV vs. Gas TCO and Solar + Powerwall 3 ROI.
"""

import argparse
import json

MODELS = {
    "model-3": {"name": "Tesla Model 3 Long Range", "msrp": 42490, "wh_mi": 250, "ice_mpg": 30, "fed_credit": 7500},
    "model-y": {"name": "Tesla Model Y Long Range", "msrp": 44990, "wh_mi": 275, "ice_mpg": 26, "fed_credit": 7500},
    "cybertruck": {"name": "Tesla Cybertruck AWD", "msrp": 79990, "wh_mi": 410, "ice_mpg": 18, "fed_credit": 7500},
    "model-s": {"name": "Tesla Model S AWD", "msrp": 74990, "wh_mi": 280, "ice_mpg": 22, "fed_credit": 0},
    "model-x": {"name": "Tesla Model X AWD", "msrp": 79990, "wh_mi": 330, "ice_mpg": 20, "fed_credit": 0},
}


def calculate(model_key: str, miles: int, kwh_rate: float, gas_price: float, state_rebate: float, years: int = 5) -> dict:
    m = MODELS[model_key]
    annual_kwh = (miles * (m["wh_mi"] / 1000.0)) / 0.88
    annual_ev_usd = annual_kwh * kwh_rate
    annual_gas_usd = (miles / m["ice_mpg"]) * gas_price
    fuel_saved = max(0.0, (annual_gas_usd - annual_ev_usd) * years)
    maint_saved = miles * 0.045 * years
    day_one = max(0.0, m["msrp"] - m["fed_credit"] - state_rebate)
    net_tco = max(0.0, day_one - fuel_saved - maint_saved)
    return {
        "model": m["name"],
        "base_msrp_usd": m["msrp"],
        "day_one_after_credits_usd": round(day_one, 2),
        "five_year_fuel_and_maint_saved_usd": round(fuel_saved + maint_saved, 2),
        "net_effective_tco_usd": round(net_tco, 2),
        "free_month_fsd_referral_link": "https://tesla.com/get-app/referral?code=justin929372",
        "solar_400_off_referral_link": "https://ts.la/justin929372",
        "interactive_web_calculator": "https://fin-hawk-dot-com.github.io/tesla-tco-solar-calculator/"
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Tesla 5-Year TCO & Solar Referral Calculator CLI")
    p.add_argument("--model", choices=list(MODELS.keys()), default="model-y")
    p.add_argument("--miles", type=int, default=12000)
    p.add_argument("--kwh", type=float, default=0.11)
    p.add_argument("--gas", type=float, default=3.65)
    p.add_argument("--state-rebate", type=float, default=0.0)
    args = p.parse_args()
    print(json.dumps(calculate(args.model, args.miles, args.kwh, args.gas, args.state_rebate), indent=2))
