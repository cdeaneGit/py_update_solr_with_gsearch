# README

---

#### About

This script finds objects that from a Fedora 3 repository and writes their associated PIDS to a text file so that the Solr index can be updated via gsearch.

#### Example

python -l localhost -p gamble

#### To Do

* As of now, this only works versus the parent namespace.
    * Add query option to work against Dublin Core collection for instances when a collection has more than one parent namespace.

