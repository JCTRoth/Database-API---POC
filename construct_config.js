// JS Code - Run it in a Browser Console
// Create JSON-Config Template used for Program-Config
//
// Replace with your config, than run it in Browser Console
// Copy the Return
// Create in the Project main Folder a .config.json
// Place the Return there - Save
//
config = {}

config.database = {} // Creates Sub Obj.
config.database.host = 'https://'
config.database.port = ''
config.database.dbName = ''
config.database.user = ''
config.database.password = ''

config.emailServer = {} // Creates Sub Obj.
config.emailServer.host = 'https://'
config.emailServer.port = ''
config.emailServer.password = ''

config.BooksApi = {} // Creates Sub Obj.
config.BooksApi.host = 'https://'

console.log(JSON.stringify(config))
