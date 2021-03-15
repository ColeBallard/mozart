const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;
const cookieParser = require('cookie-parser');

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(__dirname + '/public'))
   .use(cookieParser());

app.listen(PORT, () => {
  console.log(`Server listening on: http://localhost:${PORT}.`)
});