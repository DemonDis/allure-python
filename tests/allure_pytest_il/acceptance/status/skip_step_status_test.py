from hamcrest import assert_that
from tests.allure_pytest_il.pytest_runner import AllurePytestRunner

from allure_commons_il_test.report import has_test_case
from allure_commons_il_test.result import has_step
from allure_commons_il_test.result import with_status
from allure_commons_il_test.result import has_status_details
from allure_commons_il_test.result import with_message_contains
from allure_commons_il_test.result import with_trace_contains


def test_skip_in_step(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest
    >>> import allure

    >>> def test_skip_in_step_example():
    ...     with allure.step("Step"):
    ...         pytest.skip()
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_skip_in_step_example",
            with_status("skipped"),
            has_status_details(
                with_message_contains("Skipped")
            ),
            has_step(
                "Step",
                with_status("skipped"),
                has_status_details(
                    with_message_contains("Skipped"),
                    with_trace_contains("test_skip_in_step")
                )
            )
        )
    )
