from pathlib import Path

import requests

from aoc_mod.utilities import AocMod, get_year_and_day, parse_input


def test_set_auth_variables_session_id_set(monkeypatch):
    monkeypatch.setenv("SESSION_ID", "test_session_id")

    aoc_mod = AocMod()

    assert aoc_mod.session_id == "test_session_id"

    aoc_mod_2 = AocMod(session_id="test_session_id")

    assert aoc_mod_2.session_id == "test_session_id"


def test_get_puzzle_instructions(monkeypatch):
    def mock_get(url, cookies, timeout):
        class MockResponse:
            def __init__(self):
                self.content = (
                    "<main><article>Test Puzzle Instructions</article></main>"
                )

            def raise_for_status(self):
                pass

        return MockResponse()

    monkeypatch.setenv("SESSION_ID", "test_session_id")
    monkeypatch.setattr(requests, "get", mock_get)
    aoc_mod = AocMod()
    instructions = aoc_mod.get_puzzle_instructions(2023, 1)
    assert "Test Puzzle Instructions" in instructions


def test_get_puzzle_input(monkeypatch):
    def mock_get(url, cookies, timeout):
        class MockResponse:
            def __init__(self):
                self.text = "Test Puzzle Input"

            def raise_for_status(self):
                pass

        return MockResponse()

    monkeypatch.setenv("SESSION_ID", "test_session_id")
    monkeypatch.setattr(requests, "get", mock_get)
    aoc_mod = AocMod()
    puzzle_input = aoc_mod.get_puzzle_input(2023, 1)
    assert puzzle_input == "Test Puzzle Input"


def test_submit_answer(monkeypatch):
    def mock_post(url, data, cookies, timeout):
        class MockResponse:
            def __init__(self):
                self.text = "Test Puzzle Answer Response"
                self.content = "<article><p>Test Puzzle Answer Response</p></article>"

            def raise_for_status(self):
                pass

        return MockResponse()

    monkeypatch.setenv("SESSION_ID", "test_session_id")
    monkeypatch.setattr(requests, "post", mock_post)
    aoc_mod = AocMod()
    response = aoc_mod.submit_answer(2023, 1, 1, 12345)
    assert response == "Test Puzzle Answer Response"


def test_get_year_and_day_valid_path():
    filepath = Path("challenges/2023/day2")
    filepath2 = Path("challenges/2022/day23")

    year, day = get_year_and_day(filepath)
    assert year == 2023 and day == 2

    year, day = get_year_and_day(filepath2)
    assert year == 2022 and day == 23


def test_get_year_and_day_invalid_path():
    filepath = Path("random/file/is/here")

    year, day = get_year_and_day(filepath)
    assert not year and not day


def test_parse_input(monkeypatch):
    def mock_open(file, mode, encoding=None):
        class ManagedFile:
            def __init__(self):
                self.file = None

            def __enter__(self):
                self.file = MockFile()
                return self.file

            def __exit__(self, exc_type, exc_value, exc_traceback):
                pass

        class MockFile:
            def __init__(self):
                pass

            def read(self):
                return "this is some file data for testing"

        return ManagedFile()

    monkeypatch.setattr(Path, "open", mock_open)
    data = parse_input(Path("random_path"))

    assert data[0] == "this is some file data for testing"
