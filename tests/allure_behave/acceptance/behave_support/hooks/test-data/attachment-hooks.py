import allure
import allure_commons_il


@allure_commons_il.fixture
def before_feature(context, feature):
    allure.attach(
        "Attachment from before_feature",
        name="Dynamic attachment",
        attachment_type=allure.attachment_type.TEXT
    )
