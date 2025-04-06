pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                sh '. venv/bin/activate && python app.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }
    }

    post {
        success {
            echo '🎉 Python pipeline completed successfully!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
    }
}
