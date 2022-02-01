pipeline {
  stage('Clone the Git') {
    git 'https://github.com/zapouria/Poll-Sample-REST.git'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'SonarQubeScanner';
    sh "${scannerHome}/bin/sonar-scanner \
    -D sonar.projectKey=jenkin-test \
    -D sonar.login=admin \
    -D sonar.password=admin \
    -D sonar.exclusions=vendor/**,storage/**,resources/**,**/*.java \
    -D sonar.sources=/var/jenkins_home/workspace/test1 \
    -D sonar.host.url=http://10.0.0.54:9000"
    }
}
