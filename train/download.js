const fs = require('fs');
const spdl = require('spdl-core').default;
const path = require("path");
require('dotenv').config({path: path.join(__dirname, '/.env')});
spdl.setCredentials(process.env.CLIENT_ID, process.env.CLIENT_SECRET);

module.exports = {
  download: function(url) {
    spdl.getInfo(url).then(infos => {
      spdl(infos.url).then(stream => {
        stream.on('end', () => console.log('- dl complete -'));
        stream.pipe(fs.createWriteStream(`data/${new Date().getTime()}.mp3`));
      });
    });
  }
};