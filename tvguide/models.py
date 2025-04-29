from django.db import models

class Channel(models.Model):
    """Represents a TV channel."""
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Program(models.Model):
    """Represents a TV program scheduled on a channel."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    channel = models.ForeignKey(Channel, related_name='programs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.channel.name}"

    class Meta:
        ordering = ['start_time']
