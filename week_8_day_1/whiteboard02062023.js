function vowelReverser(sentence){
    const vowels = {"a":1, "e":1, "i":1, "o":1, "u":1}
    let letterArray = sentence.split('')
    let left = 0
    let right = letterArray.length - 1
    while (left <= right){
        if (letterArray[left] in vowels && letterArray[right] in vowels){
            [letterArray[left], letterArray[right]] = [letterArray[right], letterArray[left]]
            left += 1
            right -= 1
        }
        if (!(letterArray[left] in vowels)){
            left += 1}
        if (!(letterArray[right] in vowels)){
            right -= 1}}
    return letterArray.join('')
}

console.log(vowelReverser("hello"))