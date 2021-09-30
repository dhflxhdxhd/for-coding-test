/*
    자바스크립트로로 구현된 해시함수 오픈소스를 변형하여 구현하였습니다. 
*/ 

const crypto = require('crypto');
const fs = require('fs');
const hash = crypto.createHash('sha256')

const fileName = "index.md";
const input = fs.createReadStream(fileName);

input.on('readable',function(){
    let data = input.read();
    if(data)
        hash.update(data);
    else console.log(`${hash.digest('hex')} ${fileName}`);
})

// const pw = 'password';
// key = hash.update('abc').digest('hex');
// console.log(key);