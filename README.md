# gilbert-plugin-assetbundle
Gilbert plugin to provide AssetBundle content type.

# Overview

This povides a content type for Gilbert that uses ``webassets`` to bundle
assets.

# Usage

The `AssetBundle` content type is a `Page` with the following parameters:

- files: list
- mode: str = 'jsmin'
- output_extension = 'js'

When rendered it generates its content, sourcing its files from
'${site_root}/assets'.
