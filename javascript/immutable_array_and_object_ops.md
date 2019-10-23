## Array
#### Push
``` javascript
// mutable
array.push(1);

// immutable
array.concat(1);
[].concat(array, 1);
[...array, 1];
```

#### Pop
``` javascript
// mutable
array.pop();

// immutable
array.slice(0, -1);
```

#### Shift
``` javascript
// mutable
array.shift();

// immutable
array.slice(1);
```

#### Unshift
``` javascript
// mutable
array.unshift(1);

// immutable
[ 1, ...array ];
[].concat(1, array);
```
#### Copy an array
``` javascript
[ ... array ];
[].concat(array);
array.slice();
```

#### Sort & Reverse
``` javascript
/* sort <-> reverse */
// mutable
array.sort();

// immutable
[ ...array ].sort();
array.concat().sort();
array.slice().sort();
```

#### Splice
``` javascript
function immutableSplice(array, start, deleteCount, ...items) {
  return [...array.slice(0, start), ...items, ...array.slice(start + deleteCount)];
}
```

#### Delete
``` javascript
/* delete one element by using index */
function immutableDelete(array, index) {
  return array.slice(0, index).concat(array.slice(index+1));
}
[...array.slice(0, index), ...array.slice(index+1)];
array.filter((elem, index) => index !== target);

/* delete multiple elements by using filter */
array.filter(elem => /* some conditions */ );
```

#### Insert
``` javascript
// insert an element
[ ...array.slice(0, index), item, array.slice(index)];

// insert elements
[ ...array.slice(0, index), ...item, array.slice(index)];
```

## Object
#### Modify/Add property
``` javascript
const object = {
  selected: 'apple',
  quantity: 13,
  fruits: ['orange', 'apple', 'lemon', 'banana']
}

// modify & add property
const newObject = {
  ...object,
  selected: 'orange',
  quantity: 5,
  origin: 'imported from Spain'
}

const newObject2 = Object.assign({}, {
  ...object,
  selected: 'banana',
  quantity: 1,
  origin: 'imported from Italy'
});
```

#### Remove property
``` javascript
const object = {
  selected: 'apple',
  quantity: 13,
  fruits: ['orange', 'apple', 'lemon', 'banana']
}

const { quantity, ...newObject} = object;
console.log(newObject);
```

#### Copy an object
``` javascript
Object.assign({}, obj); // shallow copy
{ ...obj } // shallow copy
JSON.parse(JSON.stringify(object)); // deep copy
```

## Updading Nested Objects
``` javascript
// Mistake 1: Reference; Actualy, the state was directly mutated.
let nestedState = state.nestedState;
nestedState.nestedField = action.data;
{
  ...state,
  nestedState
}

// Mistake 2: top level shallow copy;
let newState = { ...state };
newState.nestedState.nestedField = action.data;

// Correct Approach: Copying all levels of nested data
{
  ...state,
  first: {
    ...state.first,
    second: {
      ...state.first.second,
      [action.someId]: {
        ...state.first.second[action.someId],
        fourth: action.someValue
      }
    }
  }
}
```

---
## Refernece
- https://vincent.billey.me/pure-javascript-immutable-array
- https://ultimatecourses.com/blog/all-about-immutable-arrays-and-objects-in-javascript
- https://wecodetheweb.com/2016/02/12/immutable-javascript-using-es6-and-beyond
- https://github.com/immutable-js/immutable-js
- https://redux.js.org/recipes/structuring-reducers/immutable-update-patterns