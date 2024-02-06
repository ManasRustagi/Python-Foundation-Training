
class user:
    def __init__(self,userid,username,password,role):
        self.userid=userid
        self.username=username
        self.password=password
        self.role=role

    @property
    def userid(self):
        return self.userid

    @userid.setter
    def userid(self, new_userid):
        self.userid = new_userid

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, new_username):
        self.username = new_username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, new_password):
        self.password = new_password

    @property
    def role(self):
        return self.role

    @role.setter
    def role(self, new_role):
        self.role = new_role