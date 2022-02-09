def runApp(){
  def postmanGet = new URL("http://10.0.0.54:9000/api/issues/search?types=BUG&componentKeys=jenkin-test&resolved=false")
  def getConnection = postmanGet.openConnection()
  getConnection.requestMethod = 'GET'
  try {
      BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(postmanGet.getInputStream()))
      String line;
      while ((line = bufferedReader.readLine()) != null) {
      println(line)
      }
    }
  assert getConnection.responseCode == 200
}

return this
