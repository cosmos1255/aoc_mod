import pytest
import requests

from aoc_mod.utilities import AocMod, AocModError


def test_set_auth_variables_session_id_set(monkeypatch):
    monkeypatch.setenv("SESSION_ID", "test_session_id")

    aoc_mod = AocMod()

    assert aoc_mod.session_id == "test_session_id"


def test_set_auth_variables_session_id_missing(monkeypatch):
    monkeypatch.delenv("SESSION_ID", raising=False)

    try:
        _ = AocMod()
        pytest.fail("did not correctly fail")
    except AocModError:
        pass


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
