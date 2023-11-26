# Telecom Customer Churn Analysis

## Overview

This project aims to analyze customer churn in a telecom company using parametric models and Customer Lifetime Value (CLV) calculations. The main objectives include building Accelerated Failure Time (AFT) models with various distributions, comparing the models, and selecting the final model. Additionally, CLV is calculated based on the chosen model, exploring CLV within different customer segments, and providing insights into factors influencing churn risk.

## Project Inclusions

1. **Parametric Models:**
   - Build AFT models with all available distributions.
   - Compare the models based on relevant metrics.
   - Visualize survival curves in a single plot for all distributions.
   - Select the final model, considering factors beyond statistical comparisons.

2. **Customer Lifetime Value (CLV):**
   - Calculate CLV per customer using the chosen model.
   - Explore CLV variations within different customer segments.

3. **Report:**
   - Interpret coefficients from the final model.
   - Identify and describe the most valuable customer segments.
   - Estimate the annual retention budget based on CLV, Survival probabilities, and the number of at-risk subscribers.
   - Provide recommendations for retention strategies beyond the model.

## Project Components

1. **Exponential.py**
   - Defines a class for an Exponential AFT Fitter.
2. **utils.py**
   - Defines the functions (dummify_dataframe and calculate_clv) used in the project.
3. **Survival_Analysis.ipynb**
    - A report summarizing findings, interpretations, and recommendations.