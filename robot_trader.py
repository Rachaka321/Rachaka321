name: Paper Trading Bot

on:
  schedule:
    - cron: '0 * * * *'  # every hour
  workflow_dispatch:      # manual trigger allowed

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install --upgrade pip && pip install -r requirements.txt

      - name: Start Paper Trading Bot
        run: |
          echo "Starting paper trading bot..."
          python robot_trader.py