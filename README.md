cri-project/
├── .env                      # Environment file for API keys
├── data/                     # Data directory for raw and processed data
│   ├── raw/                  # Raw data fetched from APIs
│   ├── processed/            # Cleaned and preprocessed data
├── notebooks/                # Jupyter notebooks for exploration and visualization
├── src/                      # Source code for the project
│   ├── __init__.py           # Makes `src` a Python package
│   ├── data_ingestion.py     # Script to fetch data from APIs
│   ├── preprocessing.py      # Script for cleaning and preprocessing data
│   ├── indicators.py         # Script to calculate derived metrics
│   ├── aggregation.py        # Script to aggregate data for the CRI
│   ├── visualization.py      # Script for plotting and visualizing the CRI
│   ├── utils.py              # Utility functions (e.g., file handling, API requests)
├── tests/                    # Unit tests for scripts
│   ├── test_data_ingestion.py
│   ├── test_preprocessing.py
│   ├── test_indicators.py
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview and instructions
└── .gitignore                # Ignore unnecessary files in version control



architecture:
Currency Risk
├── Economic Pillar
│   ├── Inflation Risk → Inflation Rate
│   ├── Growth Stability → GDP Growth Rate
│   ├── Employment Trends → Unemployment Rate
│   ├── Fiscal Health → Debt-to-GDP Ratio
├── Exchange Rate Pillar
│   ├── Exchange Rate Volatility → Std. Dev. of Exchange Rates
│   ├── Trade Balance → Current Account Balance
│   ├── Interest Rate Differentials → Domestic vs. Foreign Rates
│   ├── Market Liquidity → FX Turnover
└── Geopolitical Pillar
    ├── Political Stability → Political Stability Index
    ├── Social Unrest → Conflict Index or Unrest Incidents
    ├── Policy Predictability → Regulatory Change Frequency
    ├── Trade Relations → Trade Conflicts or Sanctions
