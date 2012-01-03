Introduction
============

Simple package which makes fancybox available in portal_javascript. This package
does not change nor define any view or templates. It basically does nothing from
the user point of view. It is usable for template developers to avoid several
fancybox libraries registered from different products.

Problems
--------

Please note, Plone often generates image URLs without extension suffix, eg.
http://host/portal/news/news-item/image_preview returns correct image to the
browser with correct content type set, but Fancybox does not handle such URLs
correctly. Fancybox competitor, Thickbox, works fine in this situation.

From FancyBox FAQ::

 6. I`m using custom urls for images (for example,
 index.php?action=dlattach;topic=3.0;attach=9;image) and FancyBox shows source
 of image. Why?
 
 FancyBox gueses content type from url but sometimes it can be wrong. The
 solution is to force your type, like so - $(".selector").fancybox({'type' :
 'image'});

Usage
-----

Fancybox requires custom invocation of the library. You must write custom
javascript which binds fancybox code to particular tag. Define your own JS file,
register it (portal_javascripts, javascript_head_slot) and use jQuery syntax to
bind fancybox to the tags::

    jq(function() {
        jq("a.fancybox").fancybox();
    });

More detailed configuration may be passed as arguments of fancybox() function.
Please read http://fancybox.net/howto chapter 4 - `Fire plugin using jQuery
selector` and Available options.
