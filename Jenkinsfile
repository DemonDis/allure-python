pipeline {
    agent { docker 'randomknowledge/docker-pyenv-tox' }
    environment {
        HOME = pwd()
    }
    stages {
        stage("Build") {
            steps {
                sh 'tox -r --workdir=/tmp -c allure-python-commons-il-test/tox.ini'
                sh 'tox -r --workdir=/tmp -c allure-python-commons-il/tox.ini'
                sh 'tox -r --workdir=/tmp -c allure-pytest/tox.ini'
            }
        }
    }
}
