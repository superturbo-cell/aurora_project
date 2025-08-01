from IPython.display import display, HTML

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>DPLA Image Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .gallery { display: flex; flex-wrap: wrap; gap: 16px; }
        .thumb { width: 180px; }
        .thumb img { width: 100%; height: auto; border: 1px solid #ccc; }
        .caption { font-size: 0.9em; margin-top: 4px; }
    </style>
</head>
<body>
    <h1>DPLA Image Gallery</h1>
    <div class="gallery">

        <div class="thumb">
            <a href="https://reflections.mndigital.org/catalog/p16022coll55:110#" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll55&CISOPTR=110" alt="['Schedule of parks, Minneapolis, Minnesota']">
            </a>
            <div class="caption">['Schedule of parks, Minneapolis, Minnesota']</div>
        </div>
        
        <div class="thumb">
            <a href="http://archive.imamuseum.org/record/13100" target="_blank">
                <img src="http://archive.imamuseum.org/record/13100/0_thumb.jpg" alt="['Percival Gallagher notes on Minnesota parks']">
            </a>
            <div class="caption">['Percival Gallagher notes on Minnesota parks']</div>
        </div>
        
        <div class="thumb">
            <a href="http://catalog.hathitrust.org/Record/007811156" target="_blank">
                <img src="https://books.google.com/books/content?id=jwr0AAAAMAAJ&printsec=frontcover&img=1&zoom=5" alt="['Minnesota Project Rediscovery, parks and open space, Mora, Minnesota']">
            </a>
            <div class="caption">['Minnesota Project Rediscovery, parks and open space, Mora, Minnesota']</div>
        </div>
        
        <div class="thumb">
            <a href="https://reflections.mndigital.org/catalog/p16022coll55:1794#" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll55&CISOPTR=1794" alt="['Minnehaha Creek, Minneapolis Parks, Minneapolis, Minnesota']">
            </a>
            <div class="caption">['Minnehaha Creek, Minneapolis Parks, Minneapolis, Minnesota']</div>
        </div>
        
        <div class="thumb">
            <a href="https://archive.mpr.org/stories/2001/07/03/minnesota-state-parks-damaged-flooding" target="_blank">
                <img src="https://www.lib.umn.edu/sites/default/files/styles/responsive-ready__1000_x_1000_/public/media/mpr-dpla-logo.png" alt="['Minnesota state parks damaged by flooding']">
            </a>
            <div class="caption">['Minnesota state parks damaged by flooding']</div>
        </div>
        
        <div class="thumb">
            <a href="http://umedia.lib.umn.edu/item/p16022coll171:239" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll171&CISOPTR=239" alt="['Gordon Parks']">
            </a>
            <div class="caption">['Gordon Parks']</div>
        </div>
        
        <div class="thumb">
            <a href="http://umedia.lib.umn.edu/item/p16022coll171:49" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll171&CISOPTR=49" alt="['Gordon Parks']">
            </a>
            <div class="caption">['Gordon Parks']</div>
        </div>
        
        <div class="thumb">
            <a href="http://umedia.lib.umn.edu/item/p16022coll175:17590" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll175&CISOPTR=17590" alt="['Parks, C.R.']">
            </a>
            <div class="caption">['Parks, C.R.']</div>
        </div>
        
        <div class="thumb">
            <a href="http://umedia.lib.umn.edu/item/p16022coll175:16556" target="_blank">
                <img src="http://cdm16022.contentdm.oclc.org/cgi-bin/thumbnail.exe?CISOROOT=/p16022coll175&CISOPTR=16556" alt="['Ritchie, Parks']">
            </a>
            <div class="caption">['Ritchie, Parks']</div>
        </div>
        
    </div>
</body>
</html>
"""

display(HTML(html_code))