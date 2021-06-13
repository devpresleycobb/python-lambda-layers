import pytest
import sys
sys.path.insert(0,'../..')


def test_lambda_handler(event, context):
    pytest.main(["-x", "tests/unit/modules"])