pipeline {
    agent {
        label 'cabbage'
    }
    environment {
        tag = sh(returnStdout: true, script: "git describe --tags --abbrev=0").trim()
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
                    docker.withRegistry("http://docker-nexus.c-atmosphere.duckdns.org", 'nexus-docker') {
                        cabbage_app.push()
                    }
                }
            }
        }
    }
}

