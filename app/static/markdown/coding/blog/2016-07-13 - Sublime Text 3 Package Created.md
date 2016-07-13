%title: Sublime Text 3 Package Created
%author: Zelphir
%date: 2016-07-13

Reluctance of the original author of a package to add some changes, which was a matter of copy & paste, which might take two minutes, caused me to fork his repository and create a new Sublime Text 3 (ST3) package this way.

The original package is `Markdown Extended`. It had issues highlighting lists properly, as discussed in this [issue](https://github.com/jonschlinkert/sublime-markdown-extended/issues/99). As you can see I already suggested the change and the code has been provided on a Stackoverflow post a long time ago. However, when I reinstalled the package recently, the bug was still not fixed.

So I forked the repository and added proper highlighting for lists as well as introduced highlighting for roman number lists, which was completely missing in `Markdown Extended`. This is good news for people using `Pandoc`, since they might want to use roman number lists at some point. You can find my repository at [https://github.com/ZelphirKaltstahl/sublime-markdown-improved](https://github.com/ZelphirKaltstahl/sublime-markdown-improved).

I am also using a modified version of the `Seti_UX` package, to make markdown files visually more pleasing, but there is no repository for those modifications yet.