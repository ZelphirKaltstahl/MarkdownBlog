% title: Installing Pandoc
% author: Zelphir
% date: 2016-05-21

This post is supposed to serve as a tutorial for installing Pandoc and all the things necessary to be ready to make use of Pandoc.

**Note:** This guide is written for Linux distributions. If you use Windows or other operating systems, the instructions in this guide might not work. I am not planning to write a guide for Windows, so you will have to look elsewhere for that.

Pandoc is a [free software](https://en.wikipedia.org/wiki/Free_software) tool under GPL license. It is very useful for creating professional documents, including theses and papers and whatever else there is. It converts documents from one file type into another. It can handle many file types and convert them into others. How does this enable you to produce professional document, you ask? Its power comes from being able to convert rather simple formats like Markdown, reStructuredText and Emacs Org-Mode into whichever other supported format, including PDFs.

Most useful for me so far was its ability to create PDF files from a Markdown source and a so called Pandoc template. It takes away the chores of working with plain TeX or LaTeX and lets you use Markdown instead most of the time, except in the optionally suppliable Pandoc template. However, while it does that, it still allows you to use TeX and any TeX packages whenever you deem it necessary. You can simply write that (La)TeX code in your Markdown file and Pandoc will take care of it. You can still do everything, you would be able to do with only LaTeX. The way this works is, that Pandoc translates your Markdown source into TeX source and then compiles a PDF using a TeX-engine specified by the user, considering what you wrote in your Pandoc Template, or what the default is. If there is TeX code in your Markdown file, Pandoc will not change it and hand it to the TeX-engine, which compiles the PDF. You are not losing any quality, by using Pandoc for creating your PDF file in comparison to writing plain LaTeX or TeX. By separating the template from your Markdown source, it encourages further separation of styling and content, as usually seen in HTML and CSS.

Pandoc translates to TeX and then compiles a PDF from it. If you want to export a PDF file, it requires you to have some TeX distribution installed on your system.

# Advantages

I will only write about advantages here, because I did not discovered any disadvantages of using Pandoc, when comparing with writing LaTeX or TeX only, yet.

* You can focus on your text content, because you will not have to deal with LaTeX or TeX stuff a lot, once you create your Pandoc template.
* You can write much faster, because you will not need to use a lot of LaTeX or TeX commands in your Markdown file and instead can use the very simple Markdown language.
* Pandoc encourages a separation of formatting (Pandoc template) and content (document source).
* Your source file will be easier to read, if you use for example Markdown or a similar simple language.
* It is easier for not so tech-savvy people to add content to your document or to colaborate with you.
* You can export your document to HTML and provide a CSS file for the styling, sort of like a counterpart for your Pandoc template when compiling a PDF file. This means you are able to have an online HTML version of a book and a PDF file, which are build from the same source. There are some free books online, which do this.
* You get a document converter for other document types as well. Heck, you can even give those MS Office users their shitty **.doc** file, if absolutely necessary, but remember [not to send them as attachement in emails](https://www.gnu.org/philosophy/po/no-word-attachments.ru-en.html) ;)

# Installing TeX Live

You could probably also use other distributions of TeX, but this is the one I used, so I will describe the process of installing Pandoc with this distribution.

## Prerequisites

There are some prerequisites for the installer to work. To verify this guide, I set up a virtual machine with the _Fedora 23 MATE-Compiz_ distribution. After installation of the OS, I needed to install the following two packages using `dnf`:

* perl-Digest-MD5
* perl-Tk (for the tlmgr GUI)
* wget
* git

## Installation

I simply follow the instructions on <http://tug.org/texlive/quickinstall.html>.

1. get `tlmgr` (TeX Live Manager) from <http://tug.org/texlive/acquire-netinstall.html>
2. su
3. (enter your super user password)
4. ./install-tl
5. Enter command: i

	Now the installer downloads all the packages from a CTAN mirror. This might take a long time. Better get yourself some tea, or do something else, while it downloads the packages. This process took 2h 3m 33s on my machine. The bottleneck is the CTAN mirrors throughput, so there is not much you can change about it.

6. Add `tlmgr` to your path by adding the following to your `~/.bashrc`:

		### texlive manager
		export PATH="/usr/local/texlive/2015/bin/x86_64-linux/:$PATH"

	You might need to search for the correct path yourself.

	After changing the `~/.bashrc` file, you will have to restart the terminal application, in order for it to notice the new `PATH` value.

## Useful Commands

* start `tlmgr` with a GUI: `tlmgr --gui`
* show all packages with available updates: `tlmgr update --list`
* update all packages: `tlmgr update --all`
* update `tlmgr` itself: `tlmgr update --self`

# Installing Stack

Stack is a tool helping you to develop Haskell programs. We will not write any Haskell code, but we want to build Pandoc, which is a Haskell program, so we will use Stack for that.

1. Get `stack` from <https://www.stackage.org/> (I took the Linux in general version).
2. Extract the archive and put the folder contained in some directory (in this example `~/bin`).
3. Add stack to your path by editing the `~/.bashrc`:

		### stack
		export PATH="$PATH:/home/user/bin/stack"

	You will have to change the user name and the stack subdirectories name accroding to your configuration and system.

	After changing the `~/.bashrc` file, you will have to restart the terminal application, in order for it to notice the new `PATH` value.

4. Run `stack setup` (only needed the first time, creates a `ghc` in `~/.local/bin`, an isolated environment, not interfering with any package manager installs).

# Installing Pandoc

We will create a new folder, where the Pandoc sources will be located.

1. Create a folder (in this example `mkdir ~/applications/pandoc`).
2. Change into the folder: `cd ~/applications/pandoc`
3. Clone the Pandoc source repository into this directory with `git clone https://github.com/jgm/pandoc.git .`
4. Run `git submodule update --init`.
5. Run `stack install`. This will install Pandoc in `~/.local/bin`. (This step might take a while.)
6. Add `pandoc` to your `PATH` variable by adding the following lines to your `~/.bashrc` file:

		### PANDOC YAY!
		export PATH="/home/user/.local/bin/:$PATH"

	You will have to change the user name accroding to your configuration.

	After changing the `~/.bashrc` file, you will have to restart the terminal application, in order for it to notice the new `PATH` value.

7. Test your Pandoc installation with `pandoc --version`. Actually you could also test your Pandoc and TeX Live distribution by compiling my [German language exercises](https://github.com/ZelphirKaltstahl/german-exercises) Markdown source to a PDF file.

## Installing pandoc-citeproc

(I will skip this step for now, since the installed Pandoc version is too new for pandoc-citeproc.)

## Installing Filters

Pandoc can be extended by filters. These filters are used when Pandoc parses your input file and are then applied to it. This enables clever people to add syntax elements to Pandoc.

One example of such filter, which is useful for scientific documents with a lot of mathematics in them is `pandoc-eqnos` There are also `pandoc-fignos` and `pandoc-tablenos` and `pandoc-xnos`, which seems to combine the three. I want to show how to use such filters in your Pandoc.

All you need to do is to install the Python package for the filters using `pip install pandoc-eqnos`. Afterwards you can run Pandoc with the parameter `--filter pandoc-eqnos`, when converting a document.

## Usage

You can find an example of Pandoc's usage on my Github repository for [German language exercises](https://github.com/ZelphirKaltstahl/german-exercises). There is also a file named `pandoc_command.txt`, which contains the call of Pandoc, which I used to compile the PDF from Markdown source. If you need more, you can find the user guide at <https://github.com/jgm/pandoc>.
