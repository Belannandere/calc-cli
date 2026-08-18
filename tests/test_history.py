import pytest
from history import save_record, load_history, show_history, clear_history, HISTORY_FILE


@pytest.fixture
def temp_history_file(tmp_path):
    
    temp_file = tmp_path / "history.txt"
    
    original = HISTORY_FILE
    
    import history
    history.HISTORY_FILE = str(temp_file)
    yield temp_file  
    
    history.HISTORY_FILE = original

def test_save_and_load_record(temp_history_file):
    
    expression = "2 + 3"
    result = 5
    save_record(expression, result)
    
    records = load_history()
    assert len(records) == 1
    assert expression in records[0]
    assert str(result) in records[0]
    
    assert records[0][:10].count('-') == 2

def test_load_empty_history(temp_history_file):
    
    records = load_history()
    assert records == []

def test_clear_history(temp_history_file):
    
    save_record("1+1", 2)
    save_record("2*3", 6)
    assert len(load_history()) == 2
    
    clear_history()
    records = load_history()
    assert records == []

def test_show_history(capsys, temp_history_file):
    
    save_record("2*2", 4)
    show_history()
    captured = capsys.readouterr()
    assert "2*2 = 4" in captured.out
    assert "--- История вычислений ---" in captured.out

def test_show_empty_history(capsys, temp_history_file):
    
    show_history()
    captured = capsys.readouterr()
    assert "История пока пуста!" in captured.out