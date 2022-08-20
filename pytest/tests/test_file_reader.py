from functions import write_to_file, read_from_file


def test_with_file(flush_file_fixture):
    write_to_file('text')
    assert read_from_file() == 'text'
