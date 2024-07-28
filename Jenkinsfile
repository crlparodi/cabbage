pipeline {
    agent {
        label 'cabbage'
    }

    stages {
        stage('build_docker') {
            steps {
                script {
                    cabbage_app = docker.build("cabbage:${env.TAG_NAME}")
                }
            }
        }
        stage('upload_nexus') {
            steps {
                script {
                    docker.withRegistry("http://192.168.122.223:8082", 'nexus-docker') {
                        cabbage_app.push()
                    }
                }
            }
        }
    }
}

