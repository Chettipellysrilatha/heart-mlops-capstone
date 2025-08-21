from pathlib import Path

def test_prep_script_exists():
    assert Path("src/prep_data.py").exists()

def test_placeholder():
    assert True