def singleton(_class):
    instance = dict()
    def create(*args, **kwargs):
        if _class not in instance:
            instance[_class] = _class(*args, **kwargs)
        return instance[_class]
    return create

@singleton
class Configuration:
    def __init__(self, base_conf=None):
        if base_conf:
            self.base_conf = dict()
            self.base_conf = base_conf


    def update(self, user_conf):
        self.base_conf.update(user_conf)



c1 = Configuration({"name":"hosein", 'lastname':"maghoul"})
print(c1.base_conf)
c1.update({'username':'hoseinlycan', 'email':'hosein.maghoul@gmail.com'})
print(c1.base_conf)


c2 = Configuration()
print(c1, c2)
print(c1 is c2)
print(c2.base_conf)