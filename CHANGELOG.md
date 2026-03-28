# Changelog

All notable changes to this autonomous instance are documented here.

## [0.3.0] - 2026-03-29
### Added
- **Amazon Manager Agent** — Introduced a specialized sub-agent for Amazon marketplace analysis and competitor tracking.
- **Keepa Toolset** — Implemented core Keepa API tools: `keepa_get_product_data`, `keepa_search`, and `keepa_get_best_sellers`.
- **Amazon Manager Skill** — Created a dedicated skill folder with best practices for interpreting Keepa data and listing health.
- **Secure Keepa Integration** — Added support for `KEEPA_API_KEY` in the secure configuration flow.

## [0.2.1] - 2026-03-29
### Added
- **Interrupted Message Persistence** — When a new message is received during processing, the previous input is now saved to the session history before cancellation. This ensures no user intent is lost during rapid-fire interactions.
- **Improved Self-Evolution Engine** — Upgraded the commit logic to automatically filter out test caches and temporary files, ensuring cleaner codebase evolution.
- **Local Evolution Tracking** — Initialized this local `CHANGELOG.md` to track our divergent development from the Ori framework.

## [0.2.0] - 2026-03-28
### Added
- Initial codebase fork from Ori (misunders2d/ori).
- Core dual-agent architecture with self-evolution capabilities.
- Telegram transport integration.
