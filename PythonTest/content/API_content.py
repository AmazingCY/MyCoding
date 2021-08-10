# -*- coding: utf-8 -*-
# @Time : 2021/8/8 23:25
# @Author : Cao yu
# @File : API_content.py
# @Software: PyCharm

import  requests

response = requests.get("http://www.baidu.com")
print(response.encoding)