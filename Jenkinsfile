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
                    sh 'docker pull mongo:latest'
                    sh 'docker run -d --name mongodb-container -p 27017:27017 mongo:latest'
                    sh 'python app.py'
                }
            }
        }
    }

    post {
        always {
            sh 'docker stop mongodb-container'
            sh 'docker rm mongodb-container'
            sh 'deactivate'
        }
    }
}
