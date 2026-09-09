# Dataset Source

## Origin
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

## License
This file is part of the SecLists repository, which is licensed under the MIT License. This means it's free to use, modify, and redistribute (including a filtered subset), as long as the original copyright/permission notice is credited somewhere in the project.

## Original size
Approximately 10,000 password entries. The file is maintained by Daniel Miessler, Jason Haddix, and g0tmi1k as part of the SecLists security research wordlist collection.

## Plan
This raw list will be filtered down to a smaller working dataset (~800 entries) for use as the comparison set in this project. Filtering will include deduplication, length-based filtering, and removal of entries not suitable for bigram/Bloom-filter comparison. The filtering process and final entry count will be documented separately once completed.

## Filtering (completed)
The raw list was deduplicated and filtered to passwords between 6 and 16 characters in length. The first 800 matching entries were kept (the source file is ordered roughly by frequency, so this retains the most common/weakest passwords). The result is stored in data/passlist.txt.