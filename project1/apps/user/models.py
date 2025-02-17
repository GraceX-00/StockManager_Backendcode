import mongoengine



#创建类
#user包含的属性
# userid(用户id)，username(用户名),userpassword(用户密码)，userphone(用户手机号)，useremail(用户邮箱)


class User(mongoengine.Document):
    userid = mongoengine.StringField(required=True)  # 用户id
    username = mongoengine.StringField(required=True)  # (用户名)
    userpassword= mongoengine.StringField(required=True)  # (用户密码)
    userphone= mongoengine.StringField(required=True)  # (用户手机号)
    useremail= mongoengine.StringField(required=True)  # (用户邮箱)


    meta = {
        "collection": "role_register",  # 指定 MongoDB 集合名称
    }
