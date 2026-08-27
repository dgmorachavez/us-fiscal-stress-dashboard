# US Fiscal Stress Dashboard

A Streamlit-based macroeconomic dashboard for analyzing stress in US Treasury markets and the interaction between fiscal conditions, monetary policy, inflation expectations, and long-term interest rates.

## Research objective

The project investigates why long-term US Treasury yields move and whether those movements can be explained primarily by inflation expectations or by other forces such as:

- real interest rates
- term premium
- Treasury issuance
- fiscal deficits and debt dynamics
- monetary policy
- liquidity conditions
- investor demand for Treasury securities

## Current dashboard

The current version retrieves the 30-Year Treasury Constant Maturity Rate from FRED and displays the most recent observations.

Current FRED series:

- DGS30 - 30-Year Treasury Constant Maturity Rate

## Planned indicators

Future versions may include:

- DGS2 - 2-Year Treasury yield
- DGS10 - 10-Year Treasury yield
- DGS30 - 30-Year Treasury yield
- 2Y-10Y and 10Y-30Y yield spreads
- breakeven inflation
- real Treasury yields
- term premium estimates
- Treasury issuance
- Federal Reserve balance sheet indicators
- fiscal deficit and debt measures

## Project structure

- pp.py - Streamlit application
- 
otebooks/ - exploratory analysis
- 
otes/ - research notes and sources
- equirements.txt - Python dependencies

## Data sources

Primary data currently comes from the Federal Reserve Bank of St. Louis FRED database.

## Status

Work in progress.
