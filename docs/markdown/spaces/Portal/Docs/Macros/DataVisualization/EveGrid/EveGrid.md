Eve Grid Macro
==============

This macro is used to show Grioview based on Eve Please notice that if
you use eve in onother server you need to make sure that, X\_DOMAINS =
'\*' in settings file. And spec.json file is allwoed to reach from
another server like:

~~~~ {.sourceCode .python}
@app.route('/docs/spec.json')
def specs():
    return send_response(None, [get_cfg()])
~~~~

Example
=======

~~~~ {.sourceCode .python}
{{evegrid:
    schema.url=192.168.9.135:5000/system
    spec.json.path=/docs/spec.json
    entity.name=eco
    datetime.fields=epoch

    column.1.data=jid
    column.1.header=Job ID
    column.1.format=<a href="/jobs/{jid}">{jid}</a>
    column.2.data=errormessage
    column.2.header=Error message
    column.3.data=occurrences
    column.3.header=Occurrences
    column.4.data=epoch
    column.4.header=Time
    column.5.data=state
    column.5.header=State
\}\}
~~~~

Output
------
