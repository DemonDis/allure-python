import os
from setuptools import setup

PACKAGE = "allure-python-commons-il"

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python :: 3.8',
]

install_requires = [
    "attrs>=16.0.0",
    "pluggy>=0.4.0",
]


def get_readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name=PACKAGE,
        # use_scm_version={"root": "..", "relative_to": __file__},
        # dynamic = ["version"],
        version='0.0.1',
        setup_requires=['setuptools_scm'],
        description=(
            "Contains the API for end users as well as helper functions and "
            "classes to build Allure adapters for Python test frameworks",
        ),
        url="https://allurereport.org/",
        project_urls={
            "Source": "https://github.com/DemonDis/allure-python",
        },
        author="Qameta Software Inc., Stanislav Seliverstov",
        author_email="sseliverstov@qameta.io",
        license="Apache-2.0",
        classifiers=classifiers,
        keywords="allure reporting report-engine",
        long_description=get_readme("README.md"),
        long_description_content_type="text/markdown",
        packages=["allure_commons_il"],
        package_dir={"allure_commons_il": 'src'},
        install_requires=install_requires,
        py_modules=['allure', 'allure_commons_il'],
        python_requires='>=3.6'
    )


if __name__ == '__main__':
    main()
