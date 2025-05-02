from backend_c import db_helper
import pytest

def test_get_details_by_date():
    res = db_helper.get_details_by_date('2024-08-02')
    assert len(res) == 6
    assert res[0]['id'] == 3
    assert res[1]['notes'].lower() == 'New Shoes'.lower()

def test_get_details_by_invalid_date():
        res = db_helper.get_details_by_date('23422')
        assert res is None