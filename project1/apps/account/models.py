import mongoengine

#创建类
#account包含的属性
# _id(系统id)，account_id(账户号)，account_name(账户名)，a_type(账户中的资产类别)，a_code(账户中的资产代码)，a_number(账户中的资产个数)


class Account(mongoengine.Document):
    account_id = mongoengine.StringField(required=True)  # 账户号
    account_name = mongoengine.StringField(required=True)  # 账户名
    a_type = mongoengine.StringField(required=True)  # 资产类别
    a_code = mongoengine.StringField(required=True)  # 资产代码
    a_number = mongoengine.StringField(required=True)  # 资产个数
    a_money0=mongoengine.StringField(required=True)

    meta = {
        "collection": "account",  # 指定 MongoDB 集合名称
        "ordering": ["-account_id"],  # 默认按账户号降序
        "indexes": ["account_id"],  # 创建索引，提高查询性能
    }
