#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:17:43 2020

@author: samueljohngomez
"""

# This is different code but yields the same result
'''
df.groupby(['key1', 'key2']).mean()

df[['data1', 'data2']].groupby([df['key1'], df['key2']]).mean()

              data1     data2
key1 key2                    
a    one   0.832807  0.423579
     two  -0.821453  1.139366
b    one  -0.978708 -0.287425
     two  -1.208338  0.915251
     
'''