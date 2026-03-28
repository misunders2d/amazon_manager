---
name: amazon-manager-skill
description: Specialized knowledge for Amazon marketplace analysis, product tracking, and Keepa data interpretation.
---

# Amazon Manager Skill

This skill provides the cognitive framework for the `AmazonManagerAgent`. It focuses on analyzing Amazon listings, identifying market opportunities, and interpreting complex Keepa data structures.

## Core Capabilities

1. **Keepa Data Analysis**: Deep-dive into ASIN history.
2. **Buy Box Tracking**: Monitoring competitor stock and pricing to optimize Buy Box ownership.
3. **Discount Identification**: Spotting Lightning Deals, Prime Exclusive discounts, and coupons.
4. **Listing Health**: Evaluating title, bullets, and image quality against category standards.

## Keepa Interpretation Rules

When analyzing Keepa data, the agent MUST follow these guidelines:
- **Prioritize Averages**: Always compare current prices to 30, 90, and 180-day averages to determine if a "deal" is legitimate or just a return to MSRP.
- **Sales Rank Velocity**: A declining sales rank (moving towards 1) indicates increasing sales volume.
- **Out of Stock (OOS) Analysis**: Identify gaps in the price graph (value -1) to spot inventory shortages in the niche.
- **Prime Exclusive Identification**: Look for specific offer-level flags to distinguish between standard discounts and Prime-only incentives.

## Usage Protocol

1. **ASIN Deep-Dive**: Use `keepa_get_product_data` to get the full picture of a product.
2. **Market Search**: Use `keepa_search` to find similar products or competitors.
3. **Supplementary Research**: Use `google_search_agent` and `web_fetch` to check external brand presence and reviews.

For detailed API indices and technical data structures, see [Keepa API Reference](references/keepa_api.md).
