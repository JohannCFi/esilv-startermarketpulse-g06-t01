# Checkpoint B

## Student

- Name: Johann Cali
- GitHub: @JohannCFi

## Contribution

- Branches: `feature/analytics`, `feature/yahoo-requirements`
- Main commits:
  - `e1c7685` — analytics layer in `src/analytics.py`
  - `a689c73` — build: add yfinance to requirements
- Pull Requests:
  - #7 `feature/analytics` -> `main` (merged, approved by @ClemRo998)
  - #9 `feature/yahoo-requirements` -> `main` (merged, approved by @ClemRo998)
- Reviewed Pull Request: #10 `docs/bloomberg-mapping` by @GabEdm974

## Work completed

Implemented the analytics layer (alignment, period return, base 100,
relative performance) and recorded the yfinance dependency in
`requirements.txt` so the Yahoo Finance provider (`src/providers/yahoo_provider.py`)
can be installed reproducibly with `pip install -r requirements.txt`.

## Main difficulty

Keeping each change inside the right branch scope: the yfinance dependency
was isolated in its own branch (`feature/yahoo-requirements`, PR #9) instead
of being mixed with the Bloomberg adapter work (`feature/bloomberg-provider`, PR #8),
so each Pull Request stays small and reviewable.

## Evidence

| File | Status |
|---|---|
| `01_pull_request.png` | present |
| `02_code_review.png` | present |
| `03_yahoo_market_data.png` | present |
| `04_instrument_benchmark.png` | present |
