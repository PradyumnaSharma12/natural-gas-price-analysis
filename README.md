# Natural Gas Price Estimation

## Overview
This project analyzes historical monthly natural gas prices and estimates the gas
price for any given date. It interpolates monthly prices to daily values and
extrapolates prices one year into the future using seasonal trends.

## Data
- Monthly end-of-month natural gas prices
- Period: October 2020 – September 2024
- File: `Nat_Gas.csv`

## Methodology
- Linear interpolation for daily price estimation
- Seasonal monthly averages for future extrapolation
- Python-based time series analysis

## Usage

Run the estimator:
```bash
python gas_price_estimator.py
