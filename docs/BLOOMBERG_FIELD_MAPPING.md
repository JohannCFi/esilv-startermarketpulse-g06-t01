# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
- Reference: Bloomberg instructor reference (external reference, not included in the team repository)
- Live connectivity: not demonstrated

The sample file declares itself as an instructor-approved fallback fixture (`"is_live_bloomberg_output": false`). Its values are illustrative teaching values reused from `data/sample/prices.csv`, not certified Bloomberg historical observations.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

The provider identifier is not the canonical ticker. MarketPulse and `analytics.py` keep receiving `AAPL` and `SP500`.

## Inputs inspected

| Series | provider_identifier | canonical_ticker | Observations | Period |
|---|---|---|---|---|
| Instrument | AAPL US Equity | AAPL | 21 | 2026-09-01 to 2026-09-30 |
| Benchmark | SPX Index | SP500 | 21 | 2026-09-01 to 2026-09-30 |

Structure: a top-level `series` list. Each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list. Each observation holds six keys: `observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value`. No missing or null value was found in either series.

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | teaching wrapper key; already a `YYYY-MM-DD` string |
| ticker | application mapping (`canonical_ticker` of the series) | AAPL or SP500, never `AAPL US Equity` / `SPX Index` |
| open | `open_value` | teaching wrapper key; number, cast to `float` |
| high | `high_value` | teaching wrapper key; number, cast to `float` |
| low | `low_value` | teaching wrapper key; number, cast to `float` |
| close | `close_value` | teaching wrapper key; number, cast to `float` |
| volume | `volume_value` | teaching wrapper key; integer, `0` for SPX Index |

Teaching wrapper key != Bloomberg LIVE field mnemonic. The keys above come from the approved sample only. No Bloomberg LIVE field name was observed in this session, so none is listed here.

## Validation

Applying this mapping to the 42 observations of the sample produces exactly the 42 rows of `data/sample/bloomberg_reference_expected.json`.

## TD10 handoff

- Access mode: APPROVED_SAMPLE (live connectivity not demonstrated)
- Target file: `src/providers/bloomberg_provider.py` (PR #8)
- Instrument identifier: `AAPL US Equity` -> canonical `AAPL`
- Benchmark identifier: `SPX Index` -> canonical `SP500`
- Date representation: `YYYY-MM-DD` string in `observation_date`
- Input structure: `series[]` -> `observations[]`, one dict per session
- Missing fields: none in the sample
- Special normalization notes: set `ticker` from `canonical_ticker`, not from `provider_identifier`; cast prices to `float` and volume to `int`; SPX Index volume is `0`, which is acceptable for an index
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
