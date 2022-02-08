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
          sh "${scannerHome}/bin/sonar-scanner \
          -D sonar.projectKey=jenkin-test \
          -D sonar.login=admin \
          -D sonar.password=admin \
          -D sonar.exclusions=vendor/**,storage/**,resources/**,**/*.java \
          -D sonar.sources=./ \
          -D sonar.host.url=http://10.0.0.54:9000"
          }
          //timeout(time: 10, unit: 'MINUTES') {
            //waitForQualityGate abortPipeline: true
          //}
        }
    }
    stage("REST to sonarqube")
    {
        steps{
            script {
                try{
                    jenkinsVar = load 'abc.groovy'
                    jenkinsVar.run()

                }catch(Exception e)
                {
                    currentBuild.result = 'FAILURE : ' + e.getMessage()
                    throw e   
                }
            }
        }
    }
}
}
