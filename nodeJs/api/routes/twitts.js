const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const Twitt = require('../models/twitt');

router.get('/',(req,res,next) =>{
  Twitt.find()
  .exec()
  .then(docs => {
  console.log(docs);
res.status(200).json(docs);
})
.catch(err =>{
  console.log(err);
  res.status(500).json({error: err});
  });
});

router.post('/',(req,res,next) => {
  const twitt = new Twitt({
    _id: new mongoose.Types.ObjectId(req.body.id),
    value: req.body.value
  });
  twitt
  .save()
  .then(resoult => {
    console.log(resoult);
    res.status(201).json({
      message: "Handling Post request to /twitts",
      createdTwitts: resoult
    })
    .catch(err =>{
      console.log(err);
      res.status(500).json({
        error: err
      });
    });
  });
});

router.get('/.twittID', (req,res,next) => {
  const id = req.params.twittID;
  Twitt.findById(id)
  .exec()
  .then(doc => {
    console.log(200).json(doc);
    if(doc){
      res.status(200).json(doc);
    }else{
      res.status(400).json({message: "No valid entry found"});
    }
  })
  .catch(err =>{
    console.log(err);
    res.status(500).json({error: err});
  });
});

router.delete('/:twittID', (req,res,next) =>{
  const id = req.params.twittID;
  Twitt.remove({_id: id})
  .exec()
  .then(resoult => {
    res.status(200).json(resoult);
  })
  .catch(err =>{
    console.log(err)
    res.status(500).json(err);
  });
});

module.exports = router;
