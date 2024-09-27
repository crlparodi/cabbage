pipeline {
    agent {
        label 'cabbage'
    }
    environment {
        tag = "${env.TAG_NAME}"
        tag2 = sh(returnStdout: true, script: "git tag --sort version:refname | tail -1").trim()
    }
    stages {
        stage('display_tag') {
            steps {
                script {
                    sh "echo ${tag}"
                    sh "echo ${tag2}"
                }
            }
        }
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
