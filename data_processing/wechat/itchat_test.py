import itchat
import time


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：", msg.text)


if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    itchat.send("文件助手你好哦", toUserName="filehelper")
    friends = itchat.get_friends()
    # print(friends)
    for friend in friends:
        # print(friend)
        # with open('info.txt', 'w')as f:
        #     f.write(str(friend))
        # if str(friend['Sex']) is '1':
        #     sex =
        print(friend)
        # print({'NickName': friend['NickName'],  'RemarkName': friend['RemarkName'], 'Sex': friend['Sex'], 'Signature': friend['Signature'], 'AttrStatus': friend['AttrStatus'], 'Province': friend['Province'], 'City': friend['City']})
    itchat.run()
# a = {'NickName': '丸子',  'RemarkName': '', 'Sex': 1, 'Signature': '足够勇敢，才会成功', 'AttrStatus': 16786425, 'Province': '广东', 'City': '广州'}
