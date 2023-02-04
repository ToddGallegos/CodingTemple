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
    const noteLetters = note.split('')
    const magazineLetters = magazine.split('')
    const magazineObject = {}
    for (const letter of magazineLetters) {
        magazineObject[letter] = magazineObject[letter] ? magazineObject[letter] + 1 : 1;
      }
    for (let i = 0; i < noteLetters.length; i++){
        console.log(magazineObject)
        if (noteLetters[i] in magazineObject){
            if (magazineObject[noteLetters[i]] == 1){
                delete magazineObject[noteLetters[i]]
            } else {
                magazineObject[noteLetters[i]] -= 1
            }
        } else if (!(noteLetters[i] in magazineObject)) {
            return false
        }
    }
    return true
}

console.log(ransom("aa","aab"))