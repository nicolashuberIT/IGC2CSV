import os
import sys
import pytest

# AI content (GitHub Copilot, 01/25/2024), verified and adapted by Nicolas Huber.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.IGC2CSV_modified.IGC2CSV_modified import IGC2CSV


@pytest.fixture
def igc2csv() -> IGC2CSV:
    return IGC2CSV()


# AI content (GitHub Copilot, 02/17/2024), verified and adapted by Nicolas Huber.
def test_initigc2csv(igc2csv: IGC2CSV) -> None:
    assert isinstance(igc2csv.recordtypes, dict)
    assert len(igc2csv.recordtypes) == 12
    assert isinstance(igc2csv.headertypes, dict)
    assert len(igc2csv.headertypes) == 1
    for value in igc2csv.recordtypes.values():
        assert callable(value)
    for value in igc2csv.headertypes.values():
        assert callable(value)

