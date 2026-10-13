# okieotsec.github.io
OT/ICS security: field comms, SCADA, and lab builds. okieotsec.com

This repository holds the source of https://okieotsec.com. It is public only so that GitHub Pages can publish it.
All rights reserved: see [LICENSE](LICENSE). Pull requests and issues are limited to the owner.

## The Resources page

`/resources/` shows the catalog from [okieotsec/ot-ics-resources](https://github.com/okieotsec/ot-ics-resources). The copy in `_data/resources.json` is a generated snapshot, never edited by hand; `_data/resources_source.json` records the repository, the exact commit and the SHA-256 of the file, and the page shows them.

To update it: edit and merge `resources.json` in the resources repository, then here run

    python3 scripts/refresh_resources.py            # latest main, or --ref <sha>
    python3 scripts/refresh_resources.py --verify   # offline: does the copy still match its record?

and open a pull request with the two changed files in `_data/`.

