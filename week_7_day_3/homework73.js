// Ransom Note
// Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
// Each letter in magazine can only be used once in ransomNote.
// Example 1:
// Input: ransomNote = "a", magazine = "b"
// Output: false
// Example 2:
// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Example 3:
// Input: ransomNote = "aa", magazine = "aab"
// Output: true

function ransom(note, magazine){
    let noteLetters = note.split('')
    let magazineLetters = magazine.split('')
    let magazineObject = {magazineLetters}
    console.log(magazineobject)
    for (let i = 0; i < noteLetters.length; i++){
        if (magazineLetters.includes(noteLetters[i])){
            delete magazineLetters[magazineLetters.indexOf(noteLetters[i])]
        } else if (!(magazineLetters.includes(noteLetters[i]))) {
            return false
        }
    }
    return true
}

console.log(ransom("abba","ccabcab"))