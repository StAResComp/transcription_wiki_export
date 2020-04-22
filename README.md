# Transcription Wiki Export

Exported data from the [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)-based
[University of St Andrews Library Transcription Platform](https://arts.st-andrews.ac.uk/transcribe/index.php?title=Main_Page).

Process outline:
1. All pages [exported](https://www.mediawiki.org/wiki/Help:Export) as XML
2. Split into separate, per-page XML files
3. MediaWiki page content extracted
4. MediaWiki content converted to HTML
5. HTML tables converted to CSV

For our immediate purpose, only the Library Borrowing Registers were of interest; other items have been filtered out.

See [process.md](process.md) for some more details.

Additional wiki pages (not corresponding to pages of the registers themselves,
but to people, books etc. mentioned in them) have been exported and processed
in `other-pages`. So the mediawiki link `[[Optics Newton]]` refers to the page
which has been exported to:

- `other-pages/xml/Optics_Newton.xml`
- `other-pages/mw/Optics_Newton.mw`
- `other-pages/html/Optics_Newton.html`

Note that spaces have been replaced with underscores in page titles/filenames.

These pages often include links to the [Biographical Register of the University
of St Andrews](https://arts.st-andrews.ac.uk/biographical-register/). The raw
TEI data for the Biographical Register is [available on
GitHub](https://github.com/StAResComp/bioreg-data/). A link to the Biographical
Register entry takes the form
`https://arts.st-andrews.ac.uk/biographical-register/data/documents/<id>`. The
corresponding raw data can be found at
`https://github.com/StAResComp/bioreg-data/blob/master/tei/idp<id>.tei`. For
example,

- https://arts.st-andrews.ac.uk/biographical-register/data/documents/1367374300

corresponds to

- https://github.com/StAResComp/bioreg-data/blob/master/tei/idp1367374300.tei

