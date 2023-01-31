//==================Exercise #1 ==========//
/*Write a function that takes in the string and the list of dog names, loops through 
the list and checks that the current name is in the string passed in. The output should be:
"Matched dog_name" if name is in the string, if no matches are present console.log "No Matches"
*/
let dog_string = "Hello Max, my name is Dog, and I have purple eyes!";
let dog_names = ["Max", "HAS", "PuRple", "dog"];

function findWords(wordList, sentence) {

    let matchArray = ["Matched "];
    let sentence_words = sentence.split(/\W+/gm);

    // START of code to match regardless of character-case (comment out for case-specific matches only)
    for (let i = 0; i < wordList.length; i++) {
        wordList[i] = wordList[i].toLowerCase();
    }

    for (let i = 0; i < sentence_words.length; i++) {
        sentence_words[i] = sentence_words[i].toLowerCase();
    }
    // END of code to match regardless of character-case (comment out for case-specific matches only)
    let wordSet = new Set(sentence_words);

    for (let i = 0; i < wordList.length; i++) {
        if (wordSet.has(wordList[i])) {
            matchArray.push(`${wordList[i]} `);
        }
    }

    if (matchArray.length > 1) {
        return matchArray.join("");
    } else {
        return "No Matches";
    }
}

console.log(findWords(dog_names, dog_string));

//Call method here with parameters

//============Exercise #2 ============//
/*Write a fucntion that takes in an array and removes every even index with a splice,
and replaces it with the string "even index" */
//Expected output
// arr1 == ["Max","Baseball","Reboot","Goku","Trucks","Rodger"]
//Output arr1 == ["even index","Baseball","even index","Goku","even index","Rodger"]

testArray = ["Max", "Baseball", "Reboot", "Goku", "Trucks", "Rodger"];

function replaceEvens(arr) {

    for (let i = 0; i < arr.length; i += 2) {
        arr[i] = "even index";
    }

    return arr;
}

console.log(replaceEvens(testArray));
