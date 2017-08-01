import os
from textwrap import dedent

def run(port=9222, page=''):
  cmd_str = dedent("""\
    '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary' \
    --user-data-dir=$(echo ~)/chrome_custom_dir/canary \
    --remote-debugging-port={} \
    {} \
    """).format(port, page)
  os.system(cmd_str)
