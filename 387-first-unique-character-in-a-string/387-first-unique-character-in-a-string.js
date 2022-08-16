/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    var mapp= {}
    for (let ele of s){
        if (mapp[ele]){
            mapp[ele]+=1
        }
        else{
            mapp[ele]=1
        }
    }
     console.log(mapp)
   for (const key of Object.keys(mapp)){
        if (mapp[key]===1){
            return s.indexOf(key)
        }
    }
    return -1
};