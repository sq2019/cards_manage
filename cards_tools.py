
import pymysql

# 连接数据库
# conn = pymysql.connect(host='10.1.10.114', user='admin', password='111111', db='testing')
# cur = conn.cursor()
# sql3 = "select * from new_card"
# cur.execute(sql3)
#
# data = cur.fetchall()
#
# for row in data:
#     print(row)
# # for cur in f:
# #     print(cur)
# conn.commit()
# conn.close()

# 创建名片表
# sql1 = ' create table new_card (id int primary key not null auto_increment, name char(20), telphone char(20), email char(50),QQ char(20)); '
#
#     try:
#         cur.execute(sql1)
#     except Exception as e:
#         print('创建表失败', e)
#     else:
#         print('创建表成功')
# 插入数据








def show_menu():
    """显示菜单"""
    print('*' * 50)
    print("欢迎使用【名片管理系统】v 1.0")
    print('')
    print('1.新增名片')
    print('2.显示全部')
    print('3.搜索名片')
    print('')
    print('0.退出系统')
    print('*' * 50)

def new_card():
    """新增名片"""
    print('-' * 50)
    print('新增名片')
    # 1. 提示用户输入名片的详情信息
    name1 = input('请输入姓名: ')

    telphone1 = input('请输入电话号码: ')
    email1 = input('请输入邮件地址: ')
    QQ1  = input('请输入qq号码: ')
    # 2.使用用户输入的信息，插入到数据库表中
    conn = pymysql.connect(host='10.1.10.114', user='admin', password='111111', db='testing')
    cur = conn.cursor()

    sql2 = "insert into new_card (name,telphone,email,qq) values (\'%s\', \'%s\', \'%s\', \'%s\')" % (name1, telphone1, email1, QQ1)

    try:
        cur.execute(sql2)
    except Exception as e:
        print('新增名片失败', e)
    else:
        print('新增名片成功')
    conn.commit()
    conn.close()
    # 3.提示用户添加成功

def show_all():
    """显示所有名片"""
    print('-' * 50)
    print('显示所有名片')
    conn = pymysql.connect(host='10.1.10.114', user='admin', password='111111', db='testing')
    cur = conn.cursor()
    sql3 = 'select name from new_card'
    try:
        cur.execute(sql3)
    except Exception as e:
        print('查询出错', e)
    data = cur.fetchall()

    for name in data:
        print(name[0])
    conn.commit()
    conn.close()


def search_card():
    """搜索名片"""
    print('-' * 50)
    print('搜索名片')
    conn = pymysql.connect(host='10.1.10.114', user='admin', password='111111', db='testing')
    cur = conn.cursor()
    name01 = input('请输入你想要搜索的姓名： ')
    telphone01 = input('请输入你想要搜索的手机号码： ')
    sql4 ='select * from new_card where name = %s and telphone = %s'
    param = (name01, telphone01)
    try:
        cur.execute(sql4, param)
    except Exception as e:
        print('出错了', e)
    data = cur.fetchall()
    print('id 姓名  电话号码    邮件      QQ')
    if data:
        for row in data:
            print(row[0], row[1], row[2], row[3], row[4])
    else:
        print('搜索结果为空')
