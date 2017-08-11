A hack tool. <br>
Open specific html file in chrome canary, watch current directory, when any change happen, update corresponding canary tab. 

Basic main function:
- watch directory (use apple's file system events api)
- update chrome tab (use chrome devtools protocol)

By python/c

Require:
- chrome canary

Limited:
- Mac OS
- Python 3.6 +

Install:
- `git clone https://github.com/badeggg/watch_hack`
- `python3 setup.py develop`

Usage: 
- `watch_hack index.html` 
- or `wah index.html` where you can chang 'index.html' to file name you want to monitor

Doc(s) about apple's file system api:
- https://developer.apple.com/library/content/documentation/Darwin/Conceptual/FSEvents_ProgGuide/Introduction/Introduction.html

Doc(s) about chrome devtools protocol: 
- https://chromedevtools.github.io/devtools-protocol/
 
