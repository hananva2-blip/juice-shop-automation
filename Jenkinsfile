pipeline {
    agent any

    triggers {
        cron('H 2 * * *')  // every night at ~02:00
    }

    environment {
        BASE_URL = 'http://juice-shop:3000'
    }

    stages {
        stage('Install') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -q -r requirements.txt'
                sh '.venv/bin/playwright install chromium'
            }
        }
        stage('Test') {
            steps {
                sh '.venv/bin/pytest --base-url $BASE_URL --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            archiveArtifacts artifacts: 'test-results/**', allowEmptyArchive: true
        }
    }
}
