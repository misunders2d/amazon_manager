# Keepa API Reference

This document provides technical details for the Keepa API used by the `AmazonManagerAgent`.

## CsvType Indices (Common)

The Keepa `csv` and `stats` arrays use these indices to categorize historical data:

| Index | Type | Description |
| :--- | :--- | :--- |
| **0** | `AMAZON` | Amazon's own price history (usually the Buy Box floor). |
| **1** | `NEW` | Marketplace New price history from 3rd party sellers. |
| **2** | `USED` | Marketplace Used price history. |
| **3** | `SALES` | Sales Rank history (closer to 1 = higher sales velocity). |
| **4** | `LISTPRICE` | Product MSRP/List Price. |
| **7** | `FBM` | Lowest Merchant-Fulfilled New price. |
| **8** | `FBA` | Lowest Fulfillment by Amazon New price. |
| **9** | `WAREHOUSE` | Amazon Warehouse Deals (Returned/Refurbished items). |
| **10** | `LIGHTNING` | Lightning Deal price (limited time promotion). |
| **18** | `BUY_BOX` | The current winning price in the Buy Box. |

## Keepa Time Conversion

Keepa uses an integer for time: **minutes since 2011-01-01 00:00:00 UTC**.

- **Conversion to Unix Timestamp**: `UnixTime = (KeepaTime + 21564000) * 60`
- **Conversion to ISO Format**: `datetime.fromtimestamp(UnixTime)`

## Status Codes & Flags

- **Value `-1`**: Indicates "Out of Stock" or no data for that timestamp.
- **`isPrimeExcl`**: (Boolean) In the `offers` array, identifies a Prime Exclusive discount.
- **`stats` Object**: Provides calculated averages for 30, 90, 180, and 365-day windows.
- **`domain` Code**: 1=US, 2=GB, 3=DE, 4=FR, 5=JP, 6=CA, 7=CN, 8=IT, 9=ES, 10=IN, 11=MX, 12=BR, 13=AU.
