from django.db import models

class conversation(models.Model):
    user_one = models.ForeignKey('users.profile', on_delete=models.CASCADE, related_name='user_one')
    user_two = models.ForeignKey('users.profile', on_delete=models.CASCADE, related_name='user_two')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_one.user.username + " | " + self.user_two.user.username
        
class message(models.Model):
    conversation = models.ForeignKey(conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey('users.profile', on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user.username + " | " + self.content