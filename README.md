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
