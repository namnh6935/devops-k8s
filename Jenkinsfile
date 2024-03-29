pipeline {
  agent {label 'worker-node-3'}
  environment {
    ENV = "dev"
    BUILD_NODE = "worker-node-3"
    MASTER_NODE = "deploy-server"
    DOCKER_HUB = "namhn89"
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
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
        dir('python/app-python') {
          sh "sudo docker build -t fastapi-$ENV:latest ."
          sh "sudo docker images"
          sh "sudo echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKER_HUB --password-stdin"
          sh "sudo docker tag fastapi-$ENV:latest $DOCKER_HUB/fastapi:$TAG"
          sh "sudo docker push $DOCKER_HUB/fastapi:$TAG"
          sh "sudo docker rmi -f $DOCKER_HUB/fastapi:$TAG"
          sh "sudo docker rmi -f fastapi-$ENV:latest"
        }
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
        sh "sudo sed -i 's|namhn89/fastapi:{tag}|namhn89/fastapi:$TAG|' python/deployment.yaml"
        sh "sudo kubectl apply -f python/deployment.yaml"
        sh "kubectl rollout status deployment/fastapi-app -n python-demo"
      }
    }
  }
}