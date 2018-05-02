const mongoose = require('mongoose');

const twittSchema = mongoose.Schema({
  _id: Number,
  value: String
});

module.exports = mongoose.model('Twitt',twittSchema);
