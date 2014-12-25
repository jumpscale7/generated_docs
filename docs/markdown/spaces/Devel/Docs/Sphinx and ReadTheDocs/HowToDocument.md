How Documentation works
=======================

This documentation gets converted from wiki syntax to rst syntax every
day by [Jenkins](http://10.101.190.1/view/JumpScale/job/Documentation).
It then pushes the rsts to the [generated\_docs
repo](https://github.com/Jumpscale/generated_docs).

[ReadTheDocs](http://jumpscale-docs.readthedocs.org/) will rebuild the
sphinx documentation everytime a commit is made to the Generated\_Docs,
thus always displaying the latest code.

To create documentation yourself
--------------------------------

~~~~ {.sourceCode .python}
jsdocs generate
~~~~

which will convert files to .rst locally and attempt to commit them to
the generated docs repo by:

-   Updating the core code base
-   Updating the documentation code base
-   Updating the generated docs
-   Running the conversion script
-   Committing changes to generated docs

Make sure that you have access to the generated\_docs repo and all merge
conflicts are resolved.