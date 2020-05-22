# moncode

Take code from the clipboard and format it for MongoDB slides.

The result looks a bit like this:

![A Python slide with lovely syntax-highlighted code.](assets/python_slide.png)

## Installing it

I recommend you use [pipx](https://pipxproject.github.io/pipx/) to install moncode as a command-line tool. If you have pipx you can install it like this:

```bash
pipx install moncode
```

If you don't want to install pipx, you can install it with pip, but it's not really recommended:

```bash
# This will install moncode into your system python:
pip install moncode
```

## Using it

Moncode is fully documented. The command you'll probably use most is `format`, like this:

### moncode format

That's the way I use it:

1. Copy Python code from my IDE
2. Run `moncode format -l python` in a terminal window. Now the syntax-highlighted Python code is in my clipboard.
3. Paste the result into Google Slides (or Powerpoint or whatever.)

There are a bunch of other ways to use the tool, taking input from stdin or a file on disk, and sending the results to stdout or a file on disk. The command options are fully documented:

```bash
$  moncode format --help
Usage: moncode format [OPTIONS]

  Format code for MongoDB slides.

  # Copy code from the clipboard, format it as RTF and then copy the result to the clipboard.
  moncode format

  # Specify the language if a guess is wrong:
  moncode format --language ruby

  # Read code from stdin and copy result to clipboard:
  cat sample_inputs/sample.js | moncode format

  # Read from sample.py and write to output.rtf:
  moncode format -i sample.py -o output.rtf

  # Read from the clipboard, and write to stdout:
  moncode format -o -

  # Format the code from the clipboard as HTML and write to output.html
  moncode format -o output.html -f html

Options:
  -l, --language TEXT      The programming language to be formatted. If not
                           supplied, this will be guessed from the file name
                           or content. It's better to supply it if you can.
                           Run `moncode languages` to see a list of supported
                           input languages.

  -i, --input FILENAME     The path to a code file to be formatted. If not
                           supplied, either code will be read from stdin, or
                           else copied from the clipboard.

  -o, --output FILENAME    The path to write output to.
  -f, --format [html|rtf]  The output format. Defaults to 'rtf' (which is good
                           for copy-pasting).

  -q, --quiet              Run quietly.
  -v, --verbose            Run loudly.
  --help                   Show this message and exit.
```

When running `moncode format`, I recommend you pass the `-l` flag, specifying the programming language of the input code. If you don't, moncode will guess the language, and likely get it wrong. What languages are supported? Glad you asked...

### moncode languages

To get a list of all the supported input languages, run `moncode languages`.
The result will look something like this...

```text
$ moncode languages
abap, abnf, ada, adl, agda, aheui, ahk, alloy, ampl, antlr, antlr-as, antlr-cpp, antlr-csharp, antlr-java, antlr-objc, antlr-perl, antlr-python, antlr-ruby, apacheconf, apl, applescript, arduino, as, as3, aspectj, aspx-cs, aspx-vb, asy, at, augeas, autoit, awk
basemake, bash, bat, bbcbasic, bbcode, bc, befunge, bib, blitzbasic, blitzmax, bnf, boa, boo, boogie, brainfuck, bst, bugs
c, c-objdump, ca65, cadl, camkes, capdl, capnp, cbmbas, ceylon, cfc, cfengine3, cfm, cfs, chai, chapel, charmci, cheetah, cirru, clay, clean, clojure, clojurescript, cmake, cobol, cobolfree, coffee-script, common-lisp, componentpascal, console, control, coq, cpp, cpp-objdump, cpsa, cr, crmsh, croc, cryptol, csharp, csound, csound-document, csound-score, css, css+django, css+erb, css+genshitext, css+lasso, css+mako, css+mozpreproc, css+myghty, css+php, css+smarty, cucumber, cuda, cypher, cython
d, d-objdump, dart, dasm16, delphi, dg, diff, django, docker, doscon, dpatch, dtd, duel, dylan, dylan-console, dylan-lid
earl-grey, easytrieve, ebnf, ec, ecl, eiffel, elixir, elm, emacs, email, erb, erl, erlang, evoque, extempore, ezhil
factor, fan, fancy, felix, fennel, fish, flatline, floscript, forth, fortran, fortranfixed, foxpro, freefem, fsharp
gap, gas, genshi, genshitext, glsl, gnuplot, go, golo, gooddata-cl, gosu, groff, groovy, gst
haml, handlebars, haskell, haxeml, hexdump, hlsl, hsail, hspec, html, html+cheetah, html+django, html+evoque, html+genshi, html+handlebars, html+lasso, html+mako, html+myghty, html+ng2, html+php, html+smarty, html+twig, html+velocity, http, hx, hybris, hylang
i6t, icon, idl, idris, iex, igor, inform6, inform7, ini, io, ioke, irc, isabelle
j, jags, jasmin, java, javascript+mozpreproc, jcl, jlcon, js, js+cheetah, js+django, js+erb, js+genshitext, js+lasso, js+mako, js+myghty, js+php, js+smarty, jsgf, json, json-object, jsonld, jsp, julia, juttle
kal, kconfig, kmsg, koka, kotlin
lagda, lasso, lcry, lean, less, lhs, lidr, lighty, limbo, liquid, live-script, llvm, llvm-mir, llvm-mir-body, logos, logtalk, lsl, lua
make, mako, maql, mask, mason, mathematica, matlab, matlabsession, md, mime, minid, modelica, modula2, monkey, monte, moocode, moon, mosel, mozhashpreproc, mozpercentpreproc, mql, ms, mscgen, mupad, mxml, myghty, mysql
nasm, ncl, nemerle, nesc, newlisp, newspeak, ng2, nginx, nim, nit, nixos, notmuch, nsis, numpy, nusmv
objdump, objdump-nasm, objective-c, objective-c++, objective-j, ocaml, octave, odin, ooc, opa, openedge
pacmanconf, pan, parasail, pawn, peg, perl, perl6, php, pig, pike, pkgconfig, plpgsql, pony, postgresql, postscript, pot, pov, powershell, praat, prolog, properties, protobuf, ps1con, psql, pug, puppet, py2tb, pycon, pypylog, pytb, python, python2
qbasic, qml, qvto
racket, ragel, ragel-c, ragel-cpp, ragel-d, ragel-em, ragel-java, ragel-objc, ragel-ruby, raw, rb, rbcon, rconsole, rd, reason, rebol, red, redcode, registry, resource, rexx, rhtml, ride, rnc, roboconf-graph, roboconf-instances, robotframework, rql, rsl, rst, rts, rust
sarl, sas, sass, sc, scala, scaml, scdoc, scheme, scilab, scss, sgf, shen, shexc, sieve, silver, slash, slim, slurm, smali, smalltalk, smarty, sml, snobol, snowball, solidity, sourceslist, sp, sparql, spec, splus, sql, sqlite3, squidconf, ssp, stan, stata, swift, swig, systemverilog
tads3, tap, tasm, tcl, tcsh, tcshcon, tea, termcap, terminfo, terraform, tex, text, thrift, todotxt, toml, trac-wiki, treetop, ts, tsql, ttl, turtle, twig, typoscript, typoscriptcssdata, typoscripthtmldata
ucode, unicon, urbiscript, usd
vala, vb.net, vbscript, vcl, vclsnippets, vctreestatus, velocity, verilog, vgl, vhdl, vim
wdiff, webidl, whiley
x10, xml, xml+cheetah, xml+django, xml+erb, xml+evoque, xml+lasso, xml+mako, xml+myghty, xml+php, xml+smarty, xml+velocity, xorg.conf, xquery, xslt, xtend, xul+mozpreproc
yaml, yaml+jinja
zeek, zephir, zig
```

Phew! That's a lot of languages, isn't it? All of these are values supported by the `-l` option to `moncode format`

## Developing

Run the following to install the project (and dev dependencies) into your active virtualenv:

```bash
pip install -e .[dev]
```
