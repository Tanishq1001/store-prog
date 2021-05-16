function inSwitch (val) {
    var num = ''
    switch(val) {
        case 1:
            num = 'alpha';
            break;
        case 2: 
            num = 'beta';
            break;
        case 3:
            num = 'gama';
            break;
    }
    return num;
}
console.log(inSwitch(2))