import os
import pytest
from app.tools.amazon.keepa import keepa_get_product_data, keepa_search, keepa_get_best_sellers

def test_keepa_tools_auth_required():
    # Ensure KEEPA_API_KEY is NOT in environment for this test
    old_key = os.environ.pop("KEEPA_API_KEY", None)
    
    try:
        res1 = keepa_get_product_data("B000000000")
        assert res1["status"] == "auth_required"
        
        res2 = keepa_search("test query")
        assert res2["status"] == "auth_required"
        
        res3 = keepa_get_best_sellers("12345")
        assert res3["status"] == "auth_required"
    finally:
        # Restore environment
        if old_key:
            os.environ["KEEPA_API_KEY"] = old_key

def test_keepa_import():
    from app.tools.amazon import keepa_get_product_data
    assert callable(keepa_get_product_data)
