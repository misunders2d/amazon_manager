import os
from datetime import datetime
from google.adk.tools.tool_context import ToolContext

def keepa_get_product_data(asin: str, tool_context: ToolContext = None) -> dict:
    """Fetches and filters product data from Keepa for a specific ASIN.

    This tool extracts comprehensive pricing history, including promotional deals,
    coupons, lightning deals, and Prime Exclusive discounts by analyzing both 
    summary stats and live offers.

    Args:
        asin (str): The Amazon Standard Identification Number (ASIN).

    Returns:
        dict: Filtered product data including price, rank, and metadata.
    """
    import httpx

    api_key = os.environ.get("KEEPA_API_KEY")
    if not api_key:
        return {
            "status": "auth_required",
            "message": "Missing KEEPA_API_KEY. Please configure it via /init or configure_integration.",
        }

    url = "https://api.keepa.com/product"
    params = {
        "key": api_key,
        "domain": "1",  # Default to US
        "asin": asin,
        "stats": "180",   # Get up to 180-day stats
        "offers": "20"    # Request up to 20 current offers
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("products"):
                return {"status": "error", "message": f"No product found for ASIN {asin}."}

            product = data["products"][0]
            stats = product.get("stats", {})

            # Helper to get price/rank from stats
            def get_stat(index, stat_type="current"):
                val_list = stats.get(stat_type)
                if val_list and len(val_list) > index:
                    val = val_list[index]
                    if val == -1:
                        return None
                    return val / 100.0 if index != 3 else val
                return None

            def keepa_minutes_to_iso(minutes):
                if minutes is None or minutes < 0:
                    return None
                try:
                    return datetime.fromtimestamp((minutes + 21564000) * 60).isoformat()
                except Exception:
                    return None

            def get_latest_price_from_csv(csv, items_per_row):
                if not csv or len(csv) < items_per_row:
                    return None
                for i in range(len(csv) - items_per_row, -1, -items_per_row):
                    p = csv[i + 1]
                    if p > 0:
                        return p / 100.0
                return None

            # Process offers for Prime Exclusive discounts
            prime_exclusive_price = None
            offers = product.get("offers", [])
            if offers:
                pe_prices = []
                for o in offers:
                    if o.get("isPrimeExcl"):
                        p = get_latest_price_from_csv(o.get("primeExclCSV"), 2)
                        if not p:
                            p = get_latest_price_from_csv(o.get("offerCSV"), 3)
                        if p:
                            pe_prices.append(p)
                if pe_prices:
                    prime_exclusive_price = min(pe_prices)

            pricing = {
                "current_amazon": get_stat(0, "current"),
                "current_new": get_stat(1, "current"),
                "current_fba": get_stat(8, "current"),
                "current_fbm": get_stat(7, "current"),
                "current_buy_box": get_stat(18, "current"),
                "current_lightning_deal": get_stat(10, "current"),
                "current_prime_exclusive": prime_exclusive_price,
                "current_list_price": get_stat(4, "current"),
                "avg_90d_amazon": get_stat(0, "avg"),
                "avg_90d_new": get_stat(1, "avg"),
                "avg_90d_buy_box": get_stat(18, "avg"),
            }

            # Best current offer calculation
            current_prices = [pricing[k] for k in pricing if "current" in k and pricing[k] is not None]
            if pricing.get("current_prime_exclusive") is not None:
                current_prices.append(pricing["current_prime_exclusive"])
                
            pricing["best_current_offer"] = min(current_prices) if current_prices else None

            filtered_data = {
                "asin": product.get("asin"),
                "title": product.get("title"),
                "brand": product.get("brand"),
                "listing_age_days": (datetime.now() - datetime.fromtimestamp((product.get("trackingSince", 0) + 21564000) * 60)).days if product.get("trackingSince") else None,
                "pricing": pricing,
                "sales_rank": {"current": get_stat(3, "current"), "avg_90d": get_stat(3, "avg")},
                "last_update": keepa_minutes_to_iso(product.get("lastUpdate"))
            }

            return {"status": "success", "data": filtered_data}

    except Exception as e:
        return {"status": "error", "message": f"Keepa API request failed: {str(e)}"}

def keepa_search(query: str, tool_context: ToolContext = None) -> dict:
    """Search for products on Amazon using Keepa's query capabilities.

    Args:
        query (str): The search query (title, brand, or keywords).

    Returns:
        dict: List of matching products with basic info.
    """
    import httpx

    api_key = os.environ.get("KEEPA_API_KEY")
    if not api_key:
        return {"status": "auth_required", "message": "Missing KEEPA_API_KEY."}

    url = "https://api.keepa.com/search"
    params = {"key": api_key, "domain": "1", "type": "product", "term": query}

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("products"):
                return {"status": "success", "products": []}

            return {"status": "success", "products": data["products"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def keepa_get_best_sellers(category_id: str, tool_context: ToolContext = None) -> dict:
    """Retrieves the best-selling products for a specific Amazon category.

    Args:
        category_id (str): The Amazon category node ID.

    Returns:
        dict: List of top ASINs in the category.
    """
    import httpx

    api_key = os.environ.get("KEEPA_API_KEY")
    if not api_key:
        return {"status": "auth_required", "message": "Missing KEEPA_API_KEY."}

    url = "https://api.keepa.com/query"
    params = {
        "key": api_key,
        "domain": "1",
        "selection": f'{{"category":"{category_id}", "sort":[[3, "asc"]]}}' 
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return {"status": "success", "asins": data.get("asins", [])}
    except Exception as e:
        return {"status": "error", "message": str(e)}
