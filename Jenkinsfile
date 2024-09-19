pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'rotem427/scores_flask'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY_CREDENTIALS = '5b7d089d-87ba-44a0-840f-c65f87a39f27'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Run Application') {
            steps {
                script {
                    bat 'docker-compose up -d --build'
                }
            }
        }

        stage('Run Tests and Add Ports') {
            steps {
                script {
                    bat '''
                        docker run -d -p 8777:5000 -v %cd%\\dummy_Scores.txt:/app/Scores.txt --name scores_test_app scores_flask
                        timeout /t 10
                        python e2e.py
                        docker stop scores_test_app
                        docker rm scores_test_app
                    '''
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    script {
                        def dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                        docker.withRegistry('', "${DOCKER_REGISTRY_CREDENTIALS}") {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}