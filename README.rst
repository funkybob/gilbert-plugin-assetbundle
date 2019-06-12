gilbert-plugin-assetbundle
==========================

Gilbert plugin to provide AssetBundle content type.

Overview
--------

This povides a content type for Gilbert that uses `webassets
<https://pypi.org/project/webassets/>`_ to bundle assets.

Usage
-----

The `AssetBundle` content type is a `Page` with the following parameters:

files: list::
    The list of files in ``assets/`` to bundle
mode: str = 'jsmin'::
    The bundling mode (or `filters` in ``webassets`` lingo)
output_extension = 'js'::
    File extension for resulting bundle.

When rendered it generates its content, sourcing its files from
'${site_root}/assets'.
