# Script to generate, make and install dictionary

# clean cache
rm -rf ~/Library/Preferences/com.apple.DictionaryServices.plist
rm -rf ~/Library/Preferences/com.apple.Dictionary.plist
rm -rf ~/Library/Caches/com.apple.DictionaryApp
rm -rf ~/Library/Caches/com.apple.DictionaryManager
rm -rf ~/Library/Caches/com.apple.Dictionary
rm -rf ~/Library/Caches/com.apple.DictionaryServices

# generate dictionary
python3 koine_greek_dictionary/ingest.py

# make and install
make
make install