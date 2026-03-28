# Changelog

All notable changes to this autonomous instance are documented here.

## [0.3.2] - 2026-03-29
### Added
- **Module Reloading** — Added `importlib.reload` to `configure_integration` to force the bot to pick up whitelist changes without a full process restart.
- **Diagnostic Logging** — Added detailed debug prints to `app/app_utils/config.py` and `app/tools/integrations.py` to trace module loading issues.

## [0.3.1] - 2026-03-29
### Changed
- **Coordinator Agent Instructions** — Explicitly mentioned `KEEPA_API_KEY` in the supported integration list to improve agent awareness.
- **Reliability Fix** — Verified and re-staged `KEEPA_API_KEY` in the global `ALLOWED_CONFIG_KEYS` whitelist to resolve configuration errors.

## [0.3.0] - 2026-03-29
### Added
- **Amazon Manager Agent** — Introduced a specialized sub-agent for Amazon marketplace analysis and competitor tracking.
- **Keepa Toolset** — Implemented core Keepa API tools: `keepa_get_product_data`, `keepa_search`, and `keepa_get_best_sellers`.
- **Amazon Manager Skill** — Created a dedicated skill folder with best practices for interpreting Keepa data and listing health.
- **Secure Keepa Integration** — Added support for `KEEPA_API_KEY` in the secure configuration flow.
