import allure
import allure_commons_il

@allure.step("Step in {caller}")
def step(caller):
    pass


@allure_commons_il.fixture
def before_all(context):
    step("before_all")


@allure_commons_il.fixture
def after_all(context):
    step("after_all")
