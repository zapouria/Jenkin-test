def runApp(){
  def postmanGet = new URL("http://10.0.0.54:9000/api/issues/search?types=BUG&componentKeys=jenkin-test&resolved=false")
  def getConnection = postmanGet.openConnection()
  getConnection.requestMethod = 'GET'
  InputStream inputStream = postmanGet.getInputStream();
  
//   String originalString = randomAlphabetic(DEFAULT_SIZE);
//   InputStream inputStream = new ByteArrayInputStream(originalString.getBytes());

  String text = new BufferedReader(
      new InputStreamReader(inputStream, StandardCharsets.UTF_8))
      .lines()
      .collect(Collectors.joining("\n"));
      
  assert getConnection.responseCode == 200
}

return this
