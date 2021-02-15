# Given a sorted array of unique values, find an element where its value is equal to the index.

중복된 원소가 없는 정렬된 배열이 있습니다. 이 배열에서 원소의 값이 원소의 인덱스 값과 같다면 프린트 하시오. 시간복잡도 O(log n).

이미 정렬되어 있고 유니크한 원소들이기 때문에 binary search로 중간 값을 비교해본 뒤 절반을 버릴 수 있는 점을 이용한다.

```javascript
function solve(input, base) {                                                                                           
 if (input.length < 1) {                                                                                               
   return -1                                                                                                           
 }                                                                                                                     

 const medium = Math.floor(input.length / 2)                                                                           
 if (input[medium] === base + medium) {                                                                                
   return base + medium                                                                                                
 }                                                                                                                     

 return input[medium] > medium                                                                                         
   ? solve( input.slice(0, medium), 0 )                                                                                
   : solve( input.slice(medium + 1), medium + 1 )                                                                      
}          
                                                                                                             
const data = [                                                                                                          
 { input: [-30, 1, 4, 60], expected: 1 },                                                                              
 { input: [0, 3, 10, 60], expected: 0 },                                                                               
 { input: [-40, -30, -20, 3], expected: 3 },                                                                           
 { input: [], expected: -1 },                                                                                          
 { input: [5, 4, 3, 2, 1], expected: -1 },                                                                             
]         

data.forEach(({ input, expected }) => {                                                                                 
 const actual = solve(input, 0)                                                                                        
 if (actual !== expected) {                                                                                            
   console.log(actual, input, expected)                                                                                
   throw new Error('Wrong answer!')                                                                                    
 }                                                                                                                     
})            
```
