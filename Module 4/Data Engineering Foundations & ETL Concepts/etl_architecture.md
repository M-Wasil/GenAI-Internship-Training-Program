# Day 15 — Data Engineering Foundations & ETL

## Use Case
A product-data pipeline collects e-commerce listings and API records, stages raw data, cleans and validates it, then loads an analytical dataset.

## Architecture

```text
Web Listings ──┐
               ├──> Extract ──> Raw Staging ──> Transform ──> Validate ──> Load ──> Analytics
REST API ──────┘
```

## Core Concepts

**ETL:** Extract data, transform it, then load the clean result.

**ELT:** Extract and load raw data first, then transform inside the target platform.

**Batch:** Process data periodically, such as hourly/daily.

**Streaming:** Process events continuously or near real-time.

**Staging:** Temporary/raw storage that preserves source data before transformation.

**Data lake:** Large-scale storage for raw/semi-structured data.

**Data warehouse:** Structured, analytics-oriented storage.

### Formats

- CSV — simple tabular, human-readable.
- JSON — nested/semi-structured API data.
- Parquet — compressed columnar format, efficient for analytics.

### Idempotency
Repeated execution with the same inputs should not create incorrect duplicates. This implementation uses stable IDs, deduplication, and deterministic replacement of output tables/files.

### Data Quality
Checks include required columns, non-null IDs, uniqueness, valid numeric ranges, parseable values, and non-empty outputs.

### Example Schema

| Field | Type | Rule |
|---|---|---|
| record_id | string | unique, required |
| name | string | required |
| description | string | required |
| price | float | >= 0 |
| source | string | required |
| processed_at | datetime | required |
