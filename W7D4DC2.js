//Write a JavaScript program that recreates the pattern below.
//Do this challenge twice: first by using one loop, then by using two 
// nested for loops (Nested means one inside the other - check out this 
// tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on 
// the internet.

//*  
//* *  
//* * *  
//* * * *  
//* * * * *
//* * * * * *
let arr=''
for (let i=1; i<=6; i++) {
    arr += '*';
    console.log(arr)
}

for (let j=1; j<=6; j++) {
    let arr2='';
    for (let k=0; k<j; k++) {
        arr2+='*'
    }
}