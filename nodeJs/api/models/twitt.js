const mongoose = require('mongoose');

const twittSchema = mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  value: String
});

module.exports = mongoose.model('Twitt',twittSchema);
