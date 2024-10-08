from hamcrest import assert_that
from tests.allure_pytest_il.pytest_runner import AllurePytestRunner

from allure_commons_il_test.report import has_test_case
from allure_commons_il_test.result import with_status
from allure_commons_il_test.result import has_status_details
from allure_commons_il_test.result import with_message_contains
from allure_commons_il_test.result import with_trace_contains


def test_xfail(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.mark.xfail()
    ... def test_xfail_example():
    ...     assert False

    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_xfail_example",
            with_status("skipped"),
            has_status_details(
                with_message_contains("XFAIL"),
                with_message_contains("AssertionError"),
                with_trace_contains("def test_xfail_example():")
            )
        )
    )


def test_xfail_with_reason_raise_mentioned_exception(
    allure_pytest_runner: AllurePytestRunner
):
    """
    >>> import pytest

    >>> @pytest.mark.xfail(raises=AssertionError, reason='Some reason')
    ... def test_xfail_with_reason_raise_mentioned_exception_example():
    ...     assert False

    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_xfail_with_reason_raise_mentioned_exception_example",
            with_status("skipped"),
            has_status_details(
                with_message_contains("XFAIL Some reason"),
                with_message_contains("AssertionError"),
                with_trace_contains(
                    "def test_xfail_with_reason_raise_mentioned_exception_example():"
                )
            )
        )
    )


def test_xfail_raise_not_mentioned_exception(
    allure_pytest_runner: AllurePytestRunner
):
    """
    >>> import pytest

    >>> @pytest.mark.xfail(raises=AssertionError)
    ... def test_xfail_raise_not_mentioned_exception_example():
    ...     raise ZeroDivisionError
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_xfail_raise_not_mentioned_exception_example",
            with_status("broken"),
            has_status_details(
                with_message_contains("ZeroDivisionError"),
                with_trace_contains(
                    "def test_xfail_raise_not_mentioned_exception_example():"
                )
            )
        )
    )


def test_xfail_do_not_raise_mentioned_exception(
    allure_pytest_runner: AllurePytestRunner
):
    """
    >>> import pytest

    >>> @pytest.mark.xfail(raises=AssertionError)
    ... def test_xfail_do_not_raise_mentioned_exception_example():
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_xfail_do_not_raise_mentioned_exception_example",
            with_status("passed"),
            has_status_details(
                with_message_contains("XPASS"),
            )
        )
    )


def test_xfail_with_reason_do_not_raise_mentioned_exception(
    allure_pytest_runner: AllurePytestRunner
):
    """
    >>> import pytest

    >>> @pytest.mark.xfail(raises=AssertionError, reason="Some reason")
    ... def test_xfail_with_reason_do_not_raise_mentioned_exception_example():
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_xfail_with_reason_do_not_raise_mentioned_exception_example",
            with_status("passed"),
            has_status_details(
                with_message_contains("XPASS Some reason"),
            )
        )
    )
