var containsDuplicate = function(nums) {
    
    let temp ={}
    
    for(let i of nums){
        if(temp[i]){
            return true;
        }
        else{
            temp[i] = true; 
        }
    }
    console.log(temp)
    
    return false
    
    
};