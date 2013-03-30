SyntaxChecker
=============

A SublimeText 2 plugin that will check the syntax of script files when saved

Ths plugin will run a command to check the syntax of your script once you will save it. The command is selected according to your file's extension.

It will NOT execute your script.

Supported languages
-------------------

* Ruby
* Perl
* PHP

Supported platforms
-------------------

This plugin has been tested on Linux platform and should work the same on OS/X or Windows platforms. It has NOT been tested ont those last two.

If you encounter some problem with OS/X or Windows, register an issue or submit a pull request on [GitHub](https://github.com/srilumpa/SyntaxChecker).

Installation
------------
**With the Package Control plugin:** The easiest way to install SyntaxChecker is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select SyntaxChecker when the list appears. The advantage of using this method is that Package Control will automatically keep SyntaxChecker up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/srilumpa/SyntaxChecker) and copy the SyntaxChecker folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone git://github.com/srilumpa/SyntaxChecker.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

Contributing
------------

If you have an issue using this plugin or if you have any suggestion, feel free to submit an [issue on GitHub](https://github.com/srilumpa/SyntaxChecker/issues) or even submit a patch.

Thanks
------

Thanks to [Edgar Gonzalez](https://github.com/edgar) for allowing me to take inspiration from his work with RubyCheckOnSave
