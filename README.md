# README

---

#### About

This script queries a Fedora 3 repository and writes the PIDs of the returned objects to a text file. The text file can then be used to update Apache Solr via [Fedora GSearch](https://github.com/fcrepo3/gsearch).

#### Options and Examples

**Options**

* -l (Specify url of Fedora instance)
* -p (Specify parent namespace of collection)
* -dcr (Specify Dublin Core Relation value - Encode spaces as %20)
* -f (Specify filename to save PIDs)

**Query using parent namespace**

python -l localhost -p gamble -f recordset.txt

**Query using dc relation**

python -l localhost -dcr Bogart%20Family

#### Using Environmental Variables

When updating GSearch with predefined environmental variables, the following keys should be set:

* export GSEARCH_USER=gsearch_user_name
* export GSEARCH_PASS=gsearch_password
* export GSEARCH_HOST=gsearch_host_name


