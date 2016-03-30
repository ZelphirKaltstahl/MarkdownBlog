# LF2 Lobby on Linux
 
To use LF2 Lobby (from [﻿﻿lf2lobby.com﻿﻿](http://www.﻿﻿lf2lobby.com﻿﻿)) with WINE, you need to install the `Microsoft Visual Basic Runtime 6`, otherwise it doesn't start and will give a message about missing `msvbvm60.dll`.

It seems necessary to proceed in the following order:

1. start Little Fighter 2
2. enter the "connect to opponent" view
3. start the LF2 Lobby
4. create a game in the LF2 Lobby
5. let everyone else connect to your game
6. connect to your game
7. start the game using the button in LF2 Lobby

Once, when I didn't do it in this order, I had the following issue:

* I entered the connect to opponent view, but no matter which IP address I entered, LF2 immediately told me it couldn't connect to the specified server.

There is one other thing you should not do:

* maximize the LF2 window before clicking "start game" in the LF2 Lobby, because you won't be able to switch to the LF2 Lobby window once LF2 is maximized and not responding because you already connected.

<br>
_(Created on 2015-01-11 by Zelphir Kaltstahl)_