sudo kubectl create namespace jenkins
sudo kubectl create -f jenkins/jenkins.yaml --namespace jenkins
sudo kubectl create -f jenkins/jenkins-service.yaml --namespace jenkins
