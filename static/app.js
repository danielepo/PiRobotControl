
function addDirection(dir) {
    var input = document.getElementById("directions");
    if (input.value === "") {
        input.value = dir;
        redrawSteps(input.value);
        return;
    }
    input.value += " " + dir;
    redrawSteps(input.value);
}
function reset() {
    document.getElementById('steps').innerHTML = "";
}
function redrawSteps(input) {
    var arr = input.split(' ');
    var spans = arr.map(function (elm) {
        switch (elm) {
            case 'f':
                return '<input type="button" class="dir up"/>';
            case 'b':
                return '<input type="button" class="dir down"/>';
            case 'l':
                return '<input type="button" class="dir left"/>';
            case 'r':
                return '<input type="button" class="dir right"/>';
        }
    }).reduce(function (acc, elm) { return acc + elm });
    document.getElementById('steps').innerHTML = spans;
}
function forward() {
    addDirection('f');
}
function backward() {
    addDirection('b');
}
function left() {
    addDirection('l');
}
function right() {
    addDirection('r');
}