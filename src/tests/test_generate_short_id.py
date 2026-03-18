from src.app.core.short_link import generate_short_id

def test_generate_short_id_length():
    short_id = generate_short_id()
    assert len(short_id) == 8

def test_generate_short_id_unique():
    ids = {generate_short_id() for _ in range(100)}
    assert len(ids) == 100