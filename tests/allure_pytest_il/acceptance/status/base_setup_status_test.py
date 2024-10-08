from hamcrest import assert_that
from tests.allure_pytest_il.pytest_runner import AllurePytestRunner

from allure_commons_il_test.report import has_test_case
from allure_commons_il_test.result import with_status
from allure_commons_il_test.result import has_status_details
from allure_commons_il_test.result import with_message_contains
from allure_commons_il_test.result import with_trace_contains
from allure_commons_il_test.container import has_container
from allure_commons_il_test.container import has_before


def test_failed_fixture(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.fixture
    ... def failed_fixture():
    ...     assert False

    >>> def test_failed_fixture_example(failed_fixture):
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_failed_fixture_example",
            with_status("failed"),
            has_status_details(
                with_message_contains("AssertionError"),
                with_trace_contains("def failed_fixture():")
            ),
            has_container(
                allure_results,
                has_before(
                    "failed_fixture",
                    with_status("failed"),
                    has_status_details(
                        with_message_contains("AssertionError"),
                        with_trace_contains("failed_fixture")
                    )
                )
            )
        )
    )


def test_broken_fixture(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.fixture
    ... def broken_fixture():
    ...     raise IndexError

    >>> def test_broken_fixture_example(broken_fixture):
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_broken_fixture_example",
            with_status("broken"),
            has_status_details(
                with_message_contains("IndexError"),
                with_trace_contains("def broken_fixture():")
            ),
            has_container(
                allure_results,
                has_before(
                    "broken_fixture",
                    with_status("broken"),
                    has_status_details(
                        with_message_contains("IndexError"),
                        with_trace_contains("broken_fixture")
                    ),
                )
            )
        )
    )


def test_skip_fixture(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.fixture
    ... def skip_fixture():
    ...     pytest.skip()

    >>> def test_skip_fixture_example(skip_fixture):
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_skip_fixture_example",
            with_status("skipped"),
            has_status_details(
                with_message_contains("Skipped")
            ),
            has_container(
                allure_results,
                has_before(
                    "skip_fixture",
                    with_status("skipped"),
                    has_status_details(
                        with_message_contains("Skipped"),
                        with_trace_contains("skip_fixture")
                    )
                )
            )
        )
    )


def test_pytest_fail_fixture(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.fixture
    ... def pytest_fail_fixture():
    ...     pytest.fail()

    >>> def test_pytest_fail_fixture_example(pytest_fail_fixture):
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_pytest_fail_fixture_example",
            with_status("failed"),
            has_status_details(
                with_message_contains("Failed"),
                with_trace_contains("def pytest_fail_fixture():")
            ),
            has_container(
                allure_results,
                has_before(
                    "pytest_fail_fixture",
                    with_status("failed"),
                    has_status_details(
                        with_message_contains("Failed"),
                        with_trace_contains("pytest_fail_fixture")
                    )
                )
            )
        )
    )


def test_pytest_fail_with_reason_fixture(allure_pytest_runner: AllurePytestRunner):
    """
    >>> import pytest

    >>> @pytest.fixture
    ... def pytest_fail_with_reason_fixture():
    ...     pytest.fail("Fail message")

    >>> def test_pytest_fail_with_reason_fixture_example(pytest_fail_with_reason_fixture):
    ...     pass
    """

    allure_results = allure_pytest_runner.run_docstring()

    assert_that(
        allure_results,
        has_test_case(
            "test_pytest_fail_with_reason_fixture_example",
            with_status("failed"),
            has_status_details(
                with_message_contains("Fail message"),
                with_trace_contains("def pytest_fail_with_reason_fixture():")
            ),
            has_container(
                allure_results,
                has_before(
                    "pytest_fail_with_reason_fixture",
                    with_status("failed"),
                    has_status_details(
                        with_message_contains("Fail message"),
                        with_trace_contains("pytest_fail_with_reason_fixture")
                    )
                )
            )
        )
    )
