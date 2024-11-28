from django.db import models

class Todo(models.Model):
    NOT_STARTED = 'NS'
    IN_PROGRESS = 'IP'
    DONE = 'D'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    id = models.AutoField(primary_key=True)  # Primary key for unique identification
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_STARTED,
    )

    def __str__(self):
        return f'{self.name} - {self.get_status_display()}'
