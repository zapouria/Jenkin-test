def postmanGet = new URL("http://0.0.0.0:9000/api/issues/search?types=BUG&componentKeys=jenkin-test&resolved=false")
def getConnection = postmanGet.openConnection()
getConnection.requestMethod = 'GET'
assert getConnection.responseCode == 200
