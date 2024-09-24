pipeline {
    agent {
        label 'cabbage'
    }
    environment {
        tag = "${env.TAG_NAME}"
    }
    stages {
        stage('build_docker') {
            when {
                expression {
                    return tag != "null";
                }
            }
            steps {
                script {
                    cabbage_app = docker.build("cabbage:${tag}")
                }
            }
        }
        stage('upload_nexus') {
            when {
                expression {
                    return tag != "null";
                }
            }
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
