pipeline {
  agent any
  stages {
    stage('Clone the Git') {
      steps{
        git 'https://github.com/zapouria/Jenkin-test.git'
      }
    }
    stage('SonarQube analysis') {
      environment {
        def scannerHome = tool 'SonarQubeScanner';
      }
      steps{
        withSonarQubeEnv('SonarQube') {
          docker.image('python:3.6').inside {
          sh 'python abc.py'
          }
          sh "${scannerHome}/bin/sonar-scanner \
          -D sonar.projectKey=jenkin-test \
          -D sonar.login=admin \
          -D sonar.password=admin \
          -D sonar.exclusions=vendor/**,storage/**,resources/**,**/*.java \
          -D sonar.sources=./ \
          -D sonar.host.url=http://10.0.0.54:9000"
          }
          timeout(time: 10, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
          }
        }
      }
  }
}
