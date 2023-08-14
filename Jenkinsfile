pipeline {
    agent any

    stages {
        stage('Preparación') {
            steps {
                script {
                    sh 'pip install virtualenv'
                    sh 'virtualenv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Ejecución') {
            steps {
                script {
                    sh 'python app.py'
                }
            }
        }
    }

    post {
        always {
            sh 'deactivate'
        }
    }
}
