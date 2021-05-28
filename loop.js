var value = 12;
console.log(value);

console.log("h");


var Index = 0;
var AnArray = [0, 1, 2, 3];

// for(Index; Index < 4; Index++){
    // console.log(AnArray[Index]);
// }


var multidimensional = [[2,3], [1,2], [4,5]];

// for(var Rows = 0; Rows < 3; Rows++){
    // for(var Columns = 0; Columns < 2; Columns++){
        // console.log(multidimensional[Rows][Columns]);
    // }
// }



var multidimensional1 = [[2,3], [1,2], [4,5]];
var Rows1 =1000
var Columns1 = 0

while(Rows1 < 3){
    console.log("Print once")
    while(Columns1 < 2){
        console.log(multidimensional1[Rows1][Columns1]);
        Columns1++
    }
    Columns1 = 0;
    Rows1++
}


var DoIndex = 100;
var DoArray = [0, 1, 2];

do{
    console.log("Print once")
    console.log(DoArray[DoIndex]);
    DoIndex++
} while(DoIndex < 3);