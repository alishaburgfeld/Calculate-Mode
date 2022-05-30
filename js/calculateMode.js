// const calculateMode = () => {
    
// }

function calculateMode(list) {
    let obj= {}
    for (let item of list) {
        obj[item]=(obj[item] || 0) +1
    }
    
    let answer=[]
    for (let key in obj) {
        if (obj[key]===Math.max(...Object.values(obj))) {
            answer.push(key)
        }
    }
    return answer
}

console.log(calculateMode(["who", "what", "where", "who"]))
console.log(calculateMode([1,2,3]))