%title: Sublime Text 3 Input Method Support
%author: Zelphir
%date: 2016-07-12

I have used Sublime Text 3 (ST3) for a long time on and off, switching between Atom, ST3, Emacs and others, searching for a solution, which is acceptable in terms of memory consumption as well as functionality. The specifics of the functionalities I require are another matter. In this post I will tell you about an issue with ST3 and how I fixed it.

First let me describe the issue. Writing in ST3 is a pleasure, with all that clever completion going on. However, what happens if you want to write Chinese in ST3? You have a problem then, because ST3 does not support inputting Chinese	characters via an input method. Once you focus the ST3 window, your cursor is in the input text area and you press whatever key combination you configured for activating the input method, this is what happens: Nothing. Your input method does not get activated, because ST3 does not support input via an input method.

Here comes the solution. Someone created a shared library, which, if loaded, enables you to use input methods in ST3. Actually the README on their Github states, that this is a solution for Ubuntu. However, it's not complicated to make it work under let's say Fedora 22. The Github repository can be found at [https://github.com/lyfeyaj/sublime-text-imfix](https://github.com/lyfeyaj/sublime-text-imfix). What follows are the necessary steps for making it work:

1. Install `Fcitx`. It is assumed you have it installed and are using it instead of other available input methods. (I did not test it with other input methods.)
2. Download the source code.
3. Extract the archive.
4. Change directory into the `src` folder of the extracted archive.
5. Compile the shared library with the command ``gcc -shared -o libsublime-imfix.so sublime-imfix.c `pkg-config --libs --cflags gtk+-2.0` -fPIC`` (assuming, that all the necessary stuff is installed).
6. Copy the created `libsublime-imfix.so` into your ST3 directory (the one, where the executable is located).
7. Copy the `subl` shell script into your ST3 directory (the one, where the executable is located).
8. Edit the `subl` shell script so that it states the correct paths for your ST3. This means that `export LD_PRELOAD=` points to your `libsublime-imfix.so` shared object and the `exec` calls your ST3 executable.

