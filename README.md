<img src="https://github.com/GloomyGhost-MosquitoSeal/SinsyPlus/blob/master/logo.jpg?raw=true" align="right" width=120 />

# SinsyPlus
Singing Voice Synthesis System based on Sinsy

[![Build status](https://ci.appveyor.com/api/projects/status/est4cx966u4fevcg?svg=true)](https://ci.appveyor.com/project/GloomyGhost-MosquitoCoil/sinsyplus)

セパレイト (Japanese):[XML](demo/3.xml)(UST by YoshikageFuckwad)
<audio controls="controls">
  <source src="demo/3.ogg" type="audio/ogg" />
Please to <a href="http://gloomyghost.com/SinsyPlus/">project</a> page listen the demo!
</audio>

This script relies on the sinsy.jp website from the Nagoya Institute of Technology which implements a HMM-based Singing Voice Synthesis System.

```bash
The HMM/DNN-Based Singing Voice Syntheis System "SinsyPlus"
Version 0.0.1 (https://github.com/740291272/SinsyPlus)
Copyright (C)2009-2018 Nagoya Institute of Technology
Copyright (C)2017-2018 GloomyGhost
All rights reserved

Usage:
        SinsyPlus [infile] [Language]
                Language:
                        Japanese:ja
                        Chinese :ch
                        English :en
        Example : sinsyplus voice.xml ja

```

## Requirements
- musescore
- curl
- numpy
- matplotlib
- requests
- scipy	
- urllib

## For Unix User 
You need to download curl before running.
```bash
sudo apt-get install curl
```
## Reference:
https://github.com/mathigatti/midi2voice
