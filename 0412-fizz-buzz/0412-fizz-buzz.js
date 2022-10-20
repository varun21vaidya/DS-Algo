/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    // const arr=[];
    // for (let i=1; i<=n; i++){
    //     if (i%15==0){
    //         arr.push('FizzBuzz')
    //     }
    //     else if (i%3==0){
    //         arr.push('Fizz')
    //     }
    //     else if (i%5==0){
    //         arr.push('Buzz')
    //     }
    //     else{
    //         arr.push(i.toString())
    //     }
    // }
    // return arr
    
    s3=0
    s5=0
    s=""
    const arr=[]
    for (let i=1; i<=n; i++){
        s3++
        s5++
        if (s3==3) {
            s+="Fizz";
            s3=0
        }
        if (s5==5) {
            s+="Buzz";
            s5=0
        }
        if (s.length===0){arr.push(i.toString())}
        else{arr.push(s)}
        s=""
    }
    return arr
};