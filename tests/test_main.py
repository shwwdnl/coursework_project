
from src.main import prints_last_5


def test_prints_last_5(capsys):
    prints_last_5()
    captured = capsys.readouterr()
    assert captured.out

