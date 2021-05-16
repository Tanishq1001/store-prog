# Javascript
## Data Types:
> It is an interprated language

```
var myname = "tansihq";

myname = 8;

let ourname = "freecodecamp";

const pi = 3.14;

//initialize 
var a

//initialize and assign
var b = 2

a = 7;
console.log(a)
```

> variables are case sensitive
> if statement
```
if (condition) {
    code;
}

if (condition1 && condition2) {
    code;
}

//or : ||
if (condition1 || condition2) {
    code;
} else if (condition) {
    code;
}else {

}
```

> switch statement
```
function inSwitch() {
    var num = ''
    switch(val) {
        case 1:         // if val === 1
            num = 'alfa';
            break;
        case 2:
            num = 'beta'
            break;
        // and so on...
    }
    return num;
}
```

```
function switchofstuf(val) {
    var answer = ''
    switch (val) {
        case a:
        answer = 'apple';
        break;
    
    }
}
```

> Objects
```
var mydog = {
    'name': 'camper'
    'age': 5
    'friends': ['evevyone']
    'family members' : ['amy', 'macy', 'carat']

//accessing values from an object:

var nameValue = mydog.name // returns 'camper'
var ageValue = mydog.age // returns 5

//another way of accessing: 
var familyValue = mydog['family members'] // used when attribute is multiple words

// updating properties

var mydog = {
    'name': 'camper'
    'age': 5
    'friends': ['evevyone']
    'family members' : ['amy', 'macy', 'carat']

mydog.name = 'harry' // changes name to harry

// add new properties

var mydog = {
    'name': 'camper'
    'age': 5
    'friends': ['evevyone']
    'family members' : ['amy', 'macy', 'carat']

mydog.bark = True
delete mydog.age // deletes property
};
```

> using objects for lookup
```
function lookup(val) {
    var answer = ''
    var lookup = {
        'alpha' : 'apple'
        'beta' : 'banana'
        'gama' : 'orange'
    };
    result = lookup[val]
    return answer
} 
console.log(lookup('alpha'))
```