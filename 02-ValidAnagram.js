/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    
    if(s.length != t.length)    return false
    
    let temp = {}
    
    for(let i of s){
        if(temp[i]){
            temp[i]=temp[i]+1
        }
        else temp[i]=1
    }
    
    for(let i of t){
        
        if(temp[i]){
            temp[i]=temp[i]-1
        }
        else temp[i]=1
    }
    
    console.log(temp)
    
    for(let i in temp){
        if(temp[i]!==0)
            return false
    }
    
    return true
    
};