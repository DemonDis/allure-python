import allure
import allure_commons_il

@allure_commons_il.fixture
def before_scenario(context, scenario):
    with allure.step("Step in before_scenario"):
        pass

@allure_commons_il.fixture
def after_scenario(context, scenario):
    with allure.step("Step in after_scenario"):
        pass
