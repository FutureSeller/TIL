#### 특정 파일의 history & diff 확인
- Repo: https://github.com/lirantal/is-website-vulnerable

<details><summary>git log -p -- [filename]</summary><p>

``` bash
$ git log -p -- index.js
commit a1a09efbb069ac230825d078eb2eab0ae9d41554                                 
 Author: RAJKUMAR S <rajkumaar2304@gmail.com>                                    
 Date:   Wed Oct 9 17:29:50 2019 +0530                                           
                                                                                 
     feat(json): print results as JSON if --json flag is passed (#10)            
                                                                                 
 diff --git a/index.js b/index.js                                                
 index 9223612..fa7fbc6 100644                                                   
 --- a/index.js                                                                  
 +++ b/index.js                                                                  
 @@ -2,10 +2,12 @@                                                               
                                                                                 
  const Audit = require('./src/Audit')                                           
  const RenderConsole = require('./src/RenderConsole')                           
 +const RenderJson = require('./src/RenderJson')                                 
  const Utils = require('./src/Utils')                                           
                                                                                 
  module.exports = {                                                             
    Audit,                                                                       
    RenderConsole,                                                               
 +  RenderJson,                                                                  
    Utils                                                                        
  }                                                                              
                                                                                 
 commit 5e00a7c58038153d272c39d3730429506ccb3b0e                                 
 Author: Edgardo Ramírez <soldiercrp@gmail.com>                                  
 Date:   Tue Oct 8 15:05:19 2019 -0500                                           
                                                                                 
     feat(cli): convert a host argument to a valid url (#7)                      
                                                                                 
 diff --git a/index.js b/index.js                                                
 index de85d0b..9223612 100644                                                   
 --- a/index.js                                                                  
 +++ b/index.js                                                                  
 @@ -2,8 +2,10 @@                                                                
                                                                                 
  const Audit = require('./src/Audit')                                           
  const RenderConsole = require('./src/RenderConsole')                           
 +const Utils = require('./src/Utils')                                           
                                                                                 
  module.exports = {                                                             
    Audit,                                                                       
 -  RenderConsole                                                                
 +  RenderConsole,                                                               
 +  Utils                                                                        
  }          
```
</p></details>

#### 커밋 사이의 log 확인
``` bash
$ git log 87585c6dd986ff605786627112838f358a52cf89..a0f57d44dc275c83346d8633a084dbd1a94263d7
commit a0f57d44dc275c83346d8633a084dbd1a94263d7
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Tue Nov 19 12:09:09 2019 +0900

    [20191119:algorithm] find closest dist btw 2 points

commit 19072544d31358785a9889dbeaab0f6a11d99c12
Author: FutureSeller <f.s3ll3r@gmail.com>
Date:   Mon Nov 18 16:27:46 2019 +0900

    [20191118:browser] building the dom faster

// commit 87585c6dd986ff605786627112838f358a52cf89 ; 이 라인은 안보임
```