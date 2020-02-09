# Koine Greek Apple Dictionary :book:
_Last built on 9th February 2020_

**To do:**
- [ ] some styling
- [ ] duplicate index issue

## Installation
You only need the `Koine Greek Dictionary.dictionary` file. Place it in `~/Library/Dictionaries`.

If you wish to rebuild the dictionary, run the following commands which will install the dictionary in the aforementionned location. `koine_greek_dictionary/ingest.py` does some data cleaning work.

[You may need to install XCode Tools. I don't remember how I did this... Google and StackOverflow were faithful friends]

```shell
source venv/bin/activate
pip install -r requirements
./make.sh
```

## Credits
Lexicon from https://github.com/tyndale/STEPBible-Data by [Tyndale House, Cambridge](https://www.TyndaleHouse.com) and its [STEP Bible](https://www.STEPBible.org).

Dictionary Development Kit from https://github.com/SebastianSzturo/Dictionary-Development-Kit.