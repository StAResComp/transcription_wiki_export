# Transcribed text

1. Export all pages to complete-export-20200406.xml
2. Copy export file to pages.xml
3. Manually edit pages.xml to remove open and closing tags and `siteinfo` element (at top of file)
4. `head -n 1 complete-export-20200406.xml > opening-tag.txt`
5. `tail -n 1 complete-export-20200406.xml > closing-tag.txt`
6. `csplit -z --prefix=page --digits=4 pages.xml /\<page\>/ '{*}'`
7. ``for f in `ls page0*`; do nf="$f".xml && cp opening-tag.txt $nf && cat $f >> $nf && cat closing-tag.txt >> $nf; done``
8. `rm page0???`
9. `for xml in page0???.xml; do xmllint --xpath '//*[local-name()="text"]/text()' $xml > $xml.mw; done`
10. ``for xml in page0???.xml; do title=`xmllint --xpath '//*[local-name()="title"]/text()' $xml | tr ' /' _` && xmllint --xpath '//*[local-name()="text"]/text()' $xml > "$title.mw"; done``
11. `for f in *.mw; do sed -i '/^&lt;/d' $f && sed -i '/^$/d' $f && sed -i '1 i\{|' $f && echo '|}' >> $f; done`
12. `for f in *.mw; do sed -i '/^|}&lt;/d'; done`
13. `rm *Swiss*`
14. `for f in *.mw; do echo $f && pandoc -f mediawiki -t html $f > "${f%.*}".html; done`
15. `for f in *.html; do python3 ./html-tables-to-csv.py $f; done`

# Images

1. Downloaded .djvu files
2. Generated PDFs using [DjView4](http://djvu.sourceforge.net/djview4.html)
3. `convert -density 600 pdf/UYLY206_4_Receipt_Book_1791-1800.pdf jpg/UYLY206_4_Receipt_Book_1791-1800_%d.jpg`


