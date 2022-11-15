const fs = require('fs');
const superagent = require('superagent');
const axios = require('axios');
const figlet = require('figlet');

const url = 'https://api.chucknorris.io/jokes/random';

figlet("Daddy Jokes", function(err,data){
    if(err){
        console.log("Something went wrong")
        console.log(err);
    }

    console.log(data);
    console.log("\nOne joke at a time :) \n\n");
});

superagent.get(url).end(function (err,resp){

    if(err) return console.log(err) && console.log(` Error Code :  ${err.status}`);

    // const parsedData = JSON.stringify(resp)
    console.log(`${resp.body.value}\n`)

})



