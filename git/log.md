Repo: https://github.com/lirantal/is-website-vulnerable

#### 특정 파일의 history & diff 확인
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