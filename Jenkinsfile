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
                    sh 'docker-compose up -d --build'
                }
            }
        }

        stage('Run Tests and Add Ports') {
            steps {
                script {
                    sh '''
                        docker run -d -p 8777:5000 -v $(pwd)/dummy_Scores.txt:/app/Scores.txt --name scores_test_app scores_flask
                        sleep 10
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
                    sh 'docker-compose down'
                    docker.withRegistry('', "${DOCKER_REGISTRY_CREDENTIALS}") {
                        dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                        dockerImage.push()
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
