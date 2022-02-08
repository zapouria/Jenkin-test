def run(){
  postmanGet = new URL("http://10.0.0.54:9000/api/issues/search?types=BUG&componentKeys=jenkin-test&resolved=false")
  getConnection = postmanGet.openConnection()
  getConnection.requestMethod = 'GET'
  assert getConnection.responseCode == 200
}
