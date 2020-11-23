import requests
import jsonpath

url = 'http://120.78.128.25:8766/futureloan/member/login'
header_login = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'}
body_login = {
    "mobile_phone": "15815541773",
    "pwd": "lemon1234"
}
res = requests.post(url=url, json=body_login, headers=header_login)
print("----login---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg1 = result.get('msg')
print("----login-----end-------------------------------------------------------------------------")


# 提取member_id/token
res1 = res.json()
res_member = jsonpath.jsonpath(res1, '$..id')[0]
res_token = jsonpath.jsonpath(res1, '$..token')[0]
# 充值
url = 'http://120.78.128.25:8766/futureloan/member/recharge'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "member_id": res_member,
    "amount": "10000"
}
res = requests.post(url=url, json=body_rec, headers=header_rec)
print("----recharge---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg2 = result.get('msg')
print("----recharge end---------------------------------------------------------------------------------")



# 提现
url = 'http://120.78.128.25:8766/futureloan/member/withdraw'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "member_id": res_member,
    "amount": "10000"
}
res = requests.post(url=url, json=body_rec, headers=header_rec)
print(res.json())
# 加标
url = 'http://120.78.128.25:8766/futureloan/loan/add'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "member_id": res_member,
    "title": "购买全栈测试课程_1",
    "amount": 500000000.00,
    "loan_rate": 1,
    "loan_term": 30,
    "loan_date_type": 2,
    "bidding_days": 1
}
res = requests.post(url=url, json=body_rec, headers=header_rec)
print("----add---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg3 = result.get('msg')
print("----add-----end-------------------------------------------------------------------------")

res2 = res.json()
loan_id = jsonpath.jsonpath(res2, '$..id')[0]
# 审核
url = 'http://120.78.128.25:8766/futureloan/loan/audit'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "loan_id": loan_id,
    "approved_or_not": "true"
}
res = requests.patch(url=url, json=body_rec, headers=header_rec)
print("----audit---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg4 = result.get('msg')
print("----audit-----end-------------------------------------------------------------------------")

# 投资
url = 'http://120.78.128.25:8766/futureloan/member/invest'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "member_id": res_member,
    "loan_id": loan_id,
    "amount": "100"
}
res = requests.post(url=url, json=body_rec, headers=header_rec)
print("----invest---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg5 = result.get('msg')
print("----invest-----end-------------------------------------------------------------------------")

# 更新昵称
url = 'http://120.78.128.25:8766/futureloan/member/update'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Content-Type': 'application/json', 'Authorization': 'Bearer' + ' ' + res_token}
body_rec = {
    "member_id": res_member,
    "reg_name": "智慧美貌檬檬"
}
res = requests.patch(url=url, json=body_rec, headers=header_rec)
print("----update---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg6 = result.get('msg')
print("----update-----end-------------------------------------------------------------------------")

# 索引
url = 'http://120.78.128.25:8766/futureloan/loans'
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2'}
body_rec={
    "pageIndex": 2,
    "pageSize": 10
}
res = requests.get(url=url, json=body_rec, headers=header_rec)
print("----loans---------------------------------------------------------------------------------")
print(res.json())
result=res.json()
real_msg7 = result.get('msg')
print("----loans-----end-------------------------------------------------------------------------")


# 获取用户信息

url = "http://120.78.128.25:8766/futureloan/member/"+str(res_member)+"/info"
header_rec = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Authorization': 'Bearer' + ' ' + res_token}
res = requests.get(url=url,headers=header_rec)
print(res.json())
result=res.json()
real_msg8 = result.get('msg')
print("----res_member/info---------------------------------------------------------------------------------")
print("----res_member/info-----end-------------------------------------------------------------------------")
if  real_msg1=='OK'and real_msg2=='OK'and real_msg3=='OK'and real_msg4=='OK'and real_msg5=='OK'and real_msg6=='OK'and real_msg7=='OK' :
    print('冒烟测试用例通过')
    final_res = 'pass'
else:
    print('冒烟测试用例不通过')
    final_res = 'fail'
print( final_res )

