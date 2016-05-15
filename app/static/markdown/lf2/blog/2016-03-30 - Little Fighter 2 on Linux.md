# Little Fighter 2 on Linux

I was told about a [Little Fighter Empire Forum](http://www.lf-empire.de/forum/) post describing the process of getting Little Fighter 2 to run under Linux. The post can be found [here](http://www.lf-empire.de/forum/showthread.php?tid=10042).

Let us summarize the information. Your system needs to have the following tools installed:

* `wine`
* `winetricks`

You need to create a _wine prefix_ or use your _default wine prefix_. Use _winetricks_ to install the following dependencies:

* `vcrun2005`
* `d3dx9` (more specific: `d3dx9_36`)
* `wmp9`

	Windows Media Player 9. It depends on some libraries which LF2 seems to depend on as well.

* `quartz`

	> `quartz` is a library with functions for `DirectShow`, a part of `DirectX`, that is responsible for playing the bgm. LF2 needs it for DirectShow to work, and then it uses the codecs from Windows Media Player. If wmp9 is not installed, the game won't run if quartz is installed.

* `devenum`

	> `Devenum` is a module that functions for the `DirectShow` API which enables the generation of dynamic information for a number of devices. This means that details on waveIN and waveOUT devices will be provided by this DLL. More info: [http://dll.paretologic.com/detail.php/devenum](http://dll.paretologic.com/detail.php/devenum)

> Without these 3 libraries \[wmp9, quartz, devenum\], LF2 bgm won't play, and the error "could not create a filter graph for this file" shows up.

The explanations for `quartz` and `devenum` dependencies were written by _MangaD_ on my other [LF2 Blog](http://lf2blog.weebly.com/).

If anyone is experiencing trouble with installing the wmp9 stuff, you might want to check out this [askubuntu link](http://askubuntu.com/questions/74690/how-to-install-32-bit-wine-on-64-bit-ubuntu/74716#74716). Basically you need to have a 32bit prefix for your wine, otherwise wine will give you trouble when trying to install wmp9 and that means the above manual for playing Little FIghter 2 on Linux wont work completely.

Furthermore MangaD mentions that d3dx9 is not required.

<br>
_(Created on 2016-03-30 by Zelphir Kaltstahl)_
