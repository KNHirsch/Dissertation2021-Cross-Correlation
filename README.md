# Diss-21: Normalized Discrete Cross-Correlation Model Development
## An Attempt to Identify Meaningful Time-Shifted Correlation Relationships Between Major Cryptocurrencies for Use in Financial Portfolio Management


# Cryptocurrency Correlation Analysis

This repository contains the code and findings of a research project that aims to explore the correlations between different cryptocurrencies using discrete cross-correlation functions. The research questions, methodology, results, and conclusions are detailed in the provided dissertation.

# Table of Contents

1. [Introduction](#introduction)
2. [Research Questions](#research-questions)
3. [Methodology](#methodology)
4. [Findings and Results](#findings-and-results)
5. [Conclusion](#conclusion)
6. [Summary of the Study](#summary-of-the-study)
7. [Code Breakdown](#code-breakdown) <!-- This is the link to your code breakdown section -->


## Introduction
Cryptocurrencies have gained significant attention in recent years, and understanding the relationships between different cryptocurrencies can have implications for portfolio management and trading strategies. This project focuses on investigating the correlations between major cryptocurrencies using a mathematical model based on discrete cross-correlation functions.

## Research Questions
The research questions addressed in this study are as follows:
- Does the proposed model effectively identify relationships between time-delayed cryptocurrency pricing data?
- Is there a dominant cryptocurrency acting as a market mover?
- Do time-delayed cross-correlations provide meaningful insights for financial portfolio management?

## Methodology
The project utilizes reputable cryptocurrency pricing data and implements a Python model to calculate discrete cross-correlations between different cryptocurrencies. The model applies time delays to identify potential time-specific correlations and determine optimal time delays for trade manipulation and portfolio management.

## Findings and Results
The findings of the study indicate:

- Bitcoin often acts as the market mover among the studied cryptocurrencies.
- Strong correlations exist between different cryptocurrencies, particularly Bitcoin, Ethereum, and Litecoin.
- Time-delayed correlations are present, but their practical implications for trading strategies and portfolio management are limited.
- Correlation patterns change over time, suggesting the need for long-term data analysis.

For detailed information and graphical representations of the findings, please refer to the complete [dissertation PDF](https://drive.google.com/file/d/1NCNtTMSytwDf03_aruw0vJIbHY8RFElb/view?usp=drive_link).


## Conclusion
This study was moderately successful in defining the correlation between 4 major cryptocurrencies. We found that strong correlations do exist; however, they are mostly defined by the market mover – Bitcoin. The study and model fell short of delivering practical, meaningful observations about the nature of time-delayed relationships between the discussed cryptocurrencies. Further iterations are needed before results can potentially be used in financial capacities.

## Summary of the Study
This paper aimed to analyze cryptocurrency pricing data to identify major time-delayed trends between 3 cryptocurrencies with respect to BTC. A model based on the Python programming language processed millions of pricing data values using cross-correlation functions. The model successfully identified generic correlations but fell short in identifying meaningful time-related trends between currencies. The histograms signal that as coins are time-shifted with respect to BTC, correlations decrease. Analyzing pricing data in smaller time increments (e.g., 30 seconds) could provide more insight into cryptocurrency's reactionary behavior. Successful cross-correlation analysis could lead to new methods of managing financial assets, and it's recommended as a stage of predictive model development.

---

**Note:** The provided content is a customized template. Please ensure that all placeholders are replaced with actual links, details, and information from your research.

# Code breakdown

## Key Aspects

### Data Loading

The script loads historical cryptocurrency price data for Bitcoin and Ethereum from CSV files.

### Data Preprocessing

The script prepares the data for analysis by selecting the closing prices of the cryptocurrencies and normalizing them.

### Loop and Analysis

The script runs a loop that iterates over different time windows of the data. Within each iteration, it calculates the cross-correlation function (DCF) between the normalized prices of Bitcoin and Ethereum with varying time delays. The DCF measures the similarity between two signals at different time lags.

### Calculation of Correlation

The script calculates the correlation between the two cryptocurrency price series using statistical calculations involving means, standard deviations, and dot products.

### Visualization and Results

The script generates scatter plots to visualize the calculated DCF values against the corresponding time delays. It also plots the normalized prices of Bitcoin and Ethereum within the selected time window. The peak DCF and its associated delay are recorded in text files.

### Window Shifting

The script shifts the analysis window by 500 data points and repeats the analysis for the next time window.

### Loop Iteration

The loop continues to analyze different time windows of the data, capturing correlations and generating plots for each window.

## Usage

1. Install the required Python libraries by running `pip install numpy pandas matplotlib sklearn`.

2. Replace the file paths in the script with the paths to your own CSV data files.

3. Run the script to perform cross-correlation analysis and generate plots.

## Conclusion

This script provides insights into the correlation patterns between Bitcoin and Ethereum over different time windows. Further iterations and refinements may be necessary for more accurate analysis and practical applications.




