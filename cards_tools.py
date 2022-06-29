
import pymysql

#连接数据库
def beta_mysql():
    conn = pymysql.connect(host='10.1.10.114', user='admin', password='111111', db='testing')
    return conn


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
    conn = beta_mysql()
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


def show_all():
    """显示所有名片"""
    print('-' * 50)
    print('显示所有名片')
    conn = beta_mysql()
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
    conn = beta_mysql()
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
        # 针对搜索到的数据进行删除和修改操作#
            del_card(row, conn)

    else:
        print('搜索结果为空')



def del_card(find_cards, conn):
   #对搜索处的对象进行删除或修改操作
    print(find_cards[1])
    print('请选择你所需要的操作')
    print('1：删除')
    print('2：修改')
    cur = conn.cursor()
    action_choice = input('输入你想要选择的操作： ')
    while True:
        if action_choice == '1':
            sql_delete = 'delete from new_card where name = %s '
            params = (find_cards[1])
            try:
                cur.execute(sql_delete, params)
            except Exception as e:
                print('删除失败', e)
            else:
                print('删除成功')
            conn.commit()   #一定要有提交的语句，否则sql不会被执行
            conn.close()
            break
        elif action_choice == '2':

            print('1：修改姓名')
            print('2：修改手机号码')
            print('3：修改邮件地址')
            print('4：修改QQ')
            a_choice = input('请输入你要修改的内容选项')
            if a_choice in ['1', '2', '3', '4']:
                if a_choice == '1':
                    name_update = input('请输入修改后的姓名： ')
                    sql_update = 'update new_card set name = %s where name = %s'
                    params = (name_update, find_cards[1])
                    # cur.execute(sql_update, params)
                if a_choice == '2':
                    telphone_update = input('请输入修改后的手机号码：')
                    sql_update = 'update new_card set telphone = %s where name = %s'
                    params = (telphone_update, find_cards[1])
                if a_choice == '3':
                    email_update = input('请输入修改后的邮件地址： ')
                    sql_update = 'update new_card set email = %s where name = %s'
                    params = (email_update, find_cards[1])
                if a_choice == '4':
                    QQ_update = input('请输入修改后的qq： ')
                    sql_update = 'update new_card set QQ = %s where name = %s'
                    params = (QQ_update, find_cards[1])
                try:
                    cur.execute(sql_update, params)
                except Exception as e:
                    print('修改失败', e)
                else:
                    print('修改成功')

            else:
                print('输入错误，无此选项')
            conn.commit()
            conn.close()
            break
        else:
            print('您输入错误，请重新输入')





