import itchat

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)  #注册对文本消息进行监听，对群聊进行监听
def print_content(msg):
    print(msg['Text']+'||来自：'+msg['FromUserName']+'群，用户：'+msg['ActualNickName'])  #页面打印，也可根据实现情况进行入库操作。  msg['Text'] 群消息；msg['FromUserName'] 群id；msg['ActualNickName'] 发群消息的用户昵称

itchat.auto_login()  # 手机扫码登录

itchat.run()