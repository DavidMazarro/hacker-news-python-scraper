from src.entry import Entry

def test_entry_title():
    assert Entry("Rust is a great language!", 1).title == "Rust is a great language!"
