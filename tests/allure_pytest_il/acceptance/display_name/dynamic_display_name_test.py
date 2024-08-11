""" ./allure-pytest-il/examples/display_name/dynamic_display_name.rst """

from hamcrest import assert_that
from tests.allure_pytest_il.pytest_runner import AllurePytestRunner

from allure_commons_il_test.report import has_test_case
from allure_commons_il_test.result import has_title


def test_dynamic_display_name(allure_pytest_runner: AllurePytestRunner):
    allure_results = allure_pytest_runner.run_docpath_examples()

    assert_that(
        allure_results,
        has_test_case(
            "test_dynamic_display_name",
            has_title("It is renamed test")
        )
    )
