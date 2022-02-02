pipeline {
  agent {docker { image 'python:3.10.1-alpine' }}
  stages {
    stage('Clone the Git') {
      steps{
        git 'https://github.com/zapouria/Poll-Sample-REST.git'
      }
    }
    stage('SonarQube analysis') {
      environment {
        def scannerHome = tool 'SonarQubeScanner';
      }
      steps{
        withSonarQubeEnv('SonarQube') {
          sh "ls -la" 
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
     stage('build') {
      steps {
        sh 'python --version'
     }
  }
}
