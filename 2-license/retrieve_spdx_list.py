"""

Retrieves SPDX license list (to be committed to repo)

"""

import pandas as pd

df = pd.read_html("https://spdx.org/licenses/")[0]

df['name'] = df['Full name']
df['short'] = df['Identifier']
df['is_osi'] = df['OSI Approved?'] == 'Y'
df['is_fsf'] = df['FSF Free/Libre?'] == 'Y'

df = df.set_index('short')
df[['name', 'is_osi', 'is_fsf']].to_json("spdx_licenses.json", orient="index")

