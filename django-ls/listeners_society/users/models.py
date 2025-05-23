from django.db import models

# first set of models

# gender constraint
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# volunteer roles constraints
VOLUNTEER_ROLES_CHOICES = [
    ('Volunteer Approver', 'Volunteer Approver'),
    ('User Support Manager', 'User Support Manager'),
    ('System Monitor', 'System Monitor'),
]

# sender type constraints
SENDER_TYPE_CHOICES = [
    ('user', 'user'),
    ('Volunteer', 'volunteer'),
]

# admin model
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50, unique= True)
    password = models.CharField(max_length=128)
    role = models.CharField(choices= VOLUNTEER_ROLES_CHOICES)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null= True, blank = True)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.admin_name

# User model
class User(models.Model):
    # auto incrementing
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    # password should store hashed password
    password = models.CharField(max_length = 128) 
    date_joined = models.DateTimeField(auto_now_add = True)
    # 1 = active, 0 = inactive
    status = models.BooleanField(default = True)
    bio = models.CharField(max_length = 255, blank = True)
    last_login = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.user_name

# volunteer model
class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key = True)
    volunteer_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    phone = models.CharField(max_length = 12)
    password = models.CharField(max_length = 128)
    gender = models.CharField(choices= GENDER_CHOICES)
    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(null= True, blank = True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default = 0.0)
    bio = models.CharField(max_length=225, blank = True)
    expertise = models.CharField(max_length= 50 )
    approved_by = models.ForeignKey(Admin, on_delete=models.CASCADE )
    approved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.volunteer_name

# chat model
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    volunteer_id = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField( default=False)

    def __str__(self):
        return f"Chat {self.chat_id}"

# chat message model
class ChatMessage(models.Model):
    ChatMessage_id = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender_id = models.PositiveIntegerField()
    message_text = models.TextField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f" ChatMessage{self.ChatMessage_id}"


# python manage.py makemigrations
# python manage.py migrate