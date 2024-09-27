pipeline {
    agent {
        label 'cabbage'
    }
    environment {
        tag = sh(returnStdout: true, script: "git describe --tags --abbrev=0").trim()
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
                    docker.withRegistry("http://docker-nexus.c-atmosphere.duckdns.org", 'nexus-docker') {
                        cabbage_app.push()
                    }
                }
            }
        }
    }
}
