# @Time    : 2020/6/30 14:39
# @Author  : 叉叉
# @email   : lovechachaf@163.com
# 1：完成充值的测试用例设计
# 2：把http请求全部复用为一个函数
# 3：写一个函数专门用来读取测试用例数据，对数据进行封装成嵌套列表
# 4：写一个run函数来执行测试用例
# 请大家参考老师的代码~在云盘，先自己写，写不出来找我要代码！
# 最好自己看视频，去理解。


# 把http请求全部复用为一个函数
import requests
def http_request(url,json,token=None,method='post'):
    hearder={'X-Lemonban-Media-Type':"lemonban.v2","Authorization":token}
    if(method=='post'):
        request_data=requests.post(url,json=json,headers=hearder)
    else:
        request_data = requests.post(url, json=json, headers=hearder)
    request_data=request_data.json()
    return request_data
