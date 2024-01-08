pipeline {
  agent {label 'build-dev'}
  environment {
    ENV = "dev"
    BUILD_NODE = "build-prod"
    MASTER_NODE = "build-dev"
    DOCKER_HUB = "namhn89"
  }

  stages {
    stage('Build Image') {
      agent {
        node {
          label "$BUILD_NODE"
        }
      }

      environment {
        TAG = sh(returnStdout: true, script: "git rev-parse -short=10 HEAD | tail -n +2").trim()
      }

      steps {
        sh "cd app"
        sh "docker build -t fastapi-$ENV:latest ."
        sh "docker images"
        sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB --password-stdin"
        sh "docker tag fastapi-$ENV:latest $DOCKER_HUB/fastapi:$TAG"
        sh "docker rmi -f $DOCKER_HUB/fastapi:$TAG"
        sh "docker rmi -f fastapi-$ENV:latest"
      }
    }
    stage('Deploy on K8s') {
      agent {
        node {
          label "$MASTER_NODE"
        }
      }
      environment {
        TAG = sh(returnStdout: true, script: "git rev-parse -short=10 HEAD | tail -n +2").trim()
      }
      steps {
      }
    }
  }
}