pipeline {
    agent {
        label 'cabbage'
    }
    environment {
        tag = ${env.TAG_NAME}
    }
    stages {
        if(tag){
            stage('build_docker') {
                steps {
                    script {
                        cabbage_app = docker.build("cabbage:${tag}")
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
        else {
            stage('skip_pipeline') {
                steps {
                    script {
                        sh 'echo "No tag detected, no pipeline launched."'
                    }
                }
            }
        }
    }
}


