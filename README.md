# README

---

#### About

This script queries a Fedora 3 repository and writes the PIDS of the returned objects to a text file. The text file can then be used to update Solr via Fedora gsearch.

#### Options and Examples

**Options**

* -l (Specify url of Fedora instance)
* -p (Specify parent namespace of collection)
* -dcr (Specify Dublin Core Relation value - Encode spaces as %20)
* -f (Specify filename to save PIDs)

**Query against parent namespace**

python -l localhost -p gamble -f recordset.txt

**Query against dc relation**

python -l localhost -dcr Bogart%20Family

#### To Do

* Add option to call authentication information of gsearch from environmental variables.

