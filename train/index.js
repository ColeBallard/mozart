const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;
const cookieParser = require('cookie-parser');

app.use(express.json({limit: '50mb'}));
app.use(express.urlencoded({ limit: '50mb', extended: true }));

app.use(express.static(__dirname + '/public'))
   .use(cookieParser());
app.use(require("./api.js"));

app.listen(PORT, () => {
  console.log(`Server listening on: http://localhost:${PORT}.`)
});