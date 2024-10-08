""" ./allure-pytest-il/examples/label/suite/module_level_custom_suite.rst """

from hamcrest import assert_that
from tests.allure_pytest_il.pytest_runner import AllurePytestRunner

from allure_commons_il_test.report import has_test_case
from allure_commons_il_test.label import has_suite


def test_module_custom_suite(allure_pytest_runner: AllurePytestRunner):
    allure_results = allure_pytest_runner.run_docpath_examples()

    assert_that(
        allure_results,
        has_test_case(
            "test_module_level_custom_suite",
            has_suite("module level suite name"),
        )
    )
