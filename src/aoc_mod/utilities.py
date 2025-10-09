"""Utility functionality and AocMod class definitions"""

import os
import time

import markdownify
import requests
from bs4 import BeautifulSoup

URL_PUZZLE_MAIN = "https://adventofcode.com/{YEAR}/day/{DAY}"
URL_PUZZLE_INPUT = f"{URL_PUZZLE_MAIN}/input"
URL_PUZZLE_ANSWER = f"{URL_PUZZLE_MAIN}/answer"


class AocModError(Exception):
    """General exception for an AOC_MOD library error"""

    def __init__(self, msg):
        super().__init__(msg)


class AocMod:
    """Main utility class for the AOC_MOD library"""

    def __init__(self, session_id: str = ""):
        """initialize AocMod class with time and auth data

        :param session_id: session-id from browser after logging into
            Advent of Code, defaults to ""
        :type session_id: str, optional
        :param year: year of AoC for puzzle data, defaults to 0
        :type year: int, optional
        :param day: day of AoC for puzzle data, defaults to 0
        :type day: int, optional
        :raises AocModError: will fail on invalid year/day or invalid
            auth data (session-id)
        """
        # set the current time
        self.curr_time = self._get_current_time()

        # set the authentication data for requests
        self.user_agent = requests.utils.default_headers()["User-Agent"]

        if session_id:
            self.session_id = session_id
        else:
            self.session_id = self._get_auth_data()

    def _get_auth_data(self) -> str:
        """will return the SESSION_ID environment variable, if set

        :raises AocModError: raise an exception if we don't have a
            SESSION_ID environment variable
        :return: the SESSION_ID env variable
        :rtype: str
        """
        try:
            return os.environ["SESSION_ID"]
        except KeyError as err:
            raise AocModError(
                "missing environment variable for authentication"
            ) from err

    def _get_current_time(self) -> time.struct_time:
        """get current local time

        :return: current local time
        :rtype: time.struct_time
        """
        return time.localtime(time.time())

    def get_puzzle_instructions(self, year: int, day: int) -> str:
        """get puzzle instructions for the entered (or current) year and day

        :param year: year of AoC puzzle, defaults to current
        :type year: int
        :param day: day of AoC puzzle, defaults to current
        :type day: int
        :raises AocModError: exception if we http request throws an error
        :return: markdownify output string of puzzle instructions
        :rtype: str
        """
        # if this function wasn't provided with a date, get current year, day
        if not year or not day:
            year = self.curr_time.tm_year
            day = self.curr_time.tm_mday

        # request the puzzle input for the current year and day
        try:
            res = requests.get(
                URL_PUZZLE_MAIN.format(YEAR=year, DAY=day),
                cookies={"session": self.session_id, "User-Agent": self.user_agent},
                timeout=5,
            )
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise AocModError("http error when getting puzzle instructions") from err

        # run the instruction output through BeautifulSoup for html parsing
        soup = BeautifulSoup(res.content, "html.parser")

        result_content = ""
        for entry in soup.main.contents:  # type: ignore
            line = str(entry).strip()
            if not line:
                continue

            result_content += line

        # turn the instructions into markdown
        return markdownify.markdownify(result_content)

    def get_puzzle_input(self, year: int = 0, day: int = 0) -> str:
        """get puzzle input for specified year and day

        :param year: yeah of the puzzle, defaults to 0
        :type year: int, optional
        :param day: day of the puzzle, defaults to 0
        :type day: int, optional
        :raises AocModError: will raise for http request error or a
            request exception
        :return: the puzzle input as a string
        :rtype: str
        """
        # if this function wasn't provided with a date, get current year, day
        if not year or not day:
            year = self.curr_time.tm_year
            day = self.curr_time.tm_mday

        # request the puzzle input for the current year and day
        try:
            res = requests.get(
                URL_PUZZLE_INPUT.format(YEAR=year, DAY=day),
                cookies={"session": self.session_id, "User-Agent": self.user_agent},
                timeout=5,
            )
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise AocModError("http error when getting puzzle input") from err
        except requests.exceptions.RequestException as err:
            raise AocModError(
                "it is likely that an invalid session key was provided when getting puzzle input"
            ) from err

        return res.text.strip()

    def submit_answer(self, year: int, day: int, level: int, answer: int) -> str:
        """submit puzzle answer for the year, day and level (part)

        :param year: year of the puzzle
        :type year: int
        :param day: day of the puzzle
        :type day: int
        :param level: puzzle level or part (either 1 or 2)
        :type level: int
        :param answer: the answer to be submitted
        :type answer: int
        :raises AocModError: will raise for http request error or a
            request exception
        :return: the result from the http post request
        :rtype: str
        """
        # submit the puzzle answer
        try:
            res = requests.post(
                URL_PUZZLE_ANSWER.format(YEAR=year, DAY=day),
                data={"level": level, "answer": answer},
                cookies={"session": self.session_id, "User-Agent": self.user_agent},
                timeout=5,
            )
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise AocModError("http error when submitting puzzle answer") from err
        except requests.exceptions.RequestException as err:
            raise AocModError(
                "an invalid session key or invalid answer during submission"
            ) from err

        # run the response output through BeautifulSoup for html parsing
        soup = BeautifulSoup(res.content, "html.parser")

        for entry in soup.article.contents:  # type: ignore
            line = str(entry)
            if not line:
                continue

            result_content = line
            break

        print(markdownify.markdownify(result_content))

        return res.text
