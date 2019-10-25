## Pure Function
- Same input ⇒ Same output (every time)
- No side effects

> Completely independent of outside state
>> immune to entire classes of bugs that have to do with shared mutable state

> non-determinism = parallel processing + mutable state

#### Quiz
<details><summary> Math.random() </summary><p>

``` javascript
// impure
Math.random(); // => 0.4011148700956255
Math.random(); // => 0.8533405303023756
Math.random(); // => 0.3550692005082965
```
</p></details>

<details><summary> const time = () => new Date().LocaleTimeString() </summary><p>

``` javascript
// impure
const time = () => new Date().toLocaleTimeString();
time(); // "오후 1:30:04"
time(); // "오후 1:30:05"
time(); // "오후 1:30:07"
```
</p></details>

<details><summary> const highpass = (cutoff, value) => value >= cutoff </summary><p>

``` javascript
// pure
const highpass = (cutoff, value) => value >= cutoff;
highpass(5, 5); // => true
highpass(5, 5); // => true
highpass(5, 5); // => true

highpass(5, 123); // true
highpass(5, 6);   // true
highpass(5, 18);  // true

highpass(5, 1);   // false
highpass(5, 3);   // false
highpass(5, 4);   // false
```
</p></details>

<details><summary> other impure example </summary><p>

```javascript
// return value changed by global state named `isChecked`
let isChecked = true;

const getItem = () => {
  if (isChecked) return 'get-checked-item';
  return 'none';
}

getItem(); // get-checked-item
getItem(); // get-checked-item

isChecked = false;

getItem(); // none
getItem(); // none
```
</p></details>

---
## Reference
https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976