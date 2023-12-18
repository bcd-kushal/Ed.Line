from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os


def validate_image_extension(value):
    allowed_extensions = ['.png', '.jpg', '.jpeg']
    ext = str(value).lower().split('.')[-1]
    if not ext in allowed_extensions:
        raise ValidationError(
            _('Invalid file format. Only PNG and JPG/JPEG are allowed.'),
            code='invalid_image'
        )
    





# =============== COURSES DATABASE ===================================================
class CourseOverview(models.Model):
    course_title = models.CharField(max_length=100, default='Some Course')
    course_thumbnail = models.ImageField(upload_to='media/static/courses/course_thumbnails/', validators=[validate_image_extension])
    course_description = models.CharField(max_length=250, default='No course description')
    course_level = models.CharField(max_length=13, default='Intermediate')
    course_id = models.CharField(primary_key=True, max_length=32)

    def give_defaults(self, *args, **kwargs):
        if not self.course_description:
            self.course_description = "No course description"
        if not self.course_title:
            self.course_description = "Some Course"

        super().save(*args,**kwargs)

    def __str__(self):
        return self.course_title





class HeaderTitles(models.Model):
    overview_id = models.ForeignKey(CourseOverview,on_delete=models.CASCADE)
    header = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    total_subcourses = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])
    header_desc = models.CharField(max_length=100)
    header_id = models.CharField(primary_key=True, max_length=32)

    def __str__(self):
        return self.header





class VideoTitles(models.Model):
    header_id = models.ForeignKey(HeaderTitles,on_delete=models.CASCADE)
    overview_id = models.ForeignKey(CourseOverview,on_delete=models.CASCADE)
    vid_title = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    vid_length = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30*60*1000)])
    vid_id = models.OneToOneField('Videos', on_delete=models.CASCADE, primary_key=True, max_length=32)

    def __str__(self):
        return self.vid_title






class Videos(models.Model):
    overview_id = models.ForeignKey(CourseOverview,on_delete=models.CASCADE)
    video = models.FileField(upload_to='media/videos/')

    def __str__(self):
        return self.overview_id


        


# =============== EDUCATOR PROFILE PICTURES ===================================================
class educator_pictures(models.Model):
    mobile = models.CharField(max_length=11, primary_key=True)
    image = models.ImageField(upload_to='media/static/educator_profile_pictures/', validators=[validate_image_extension])
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    



@receiver(pre_save, sender=educator_pictures)
def delete_previous_image(sender, instance, **kwargs):
    # Check if the instance already exists in the database
    if instance.pk:
        try:
            # Retrieve the previous instance from the database
            previous_instance = educator_pictures.objects.get(pk=instance.pk)

            # Check if the image has changed
            if previous_instance.image and previous_instance.image != instance.image:
                # Delete the previous image file
                if os.path.isfile(previous_instance.image.path):
                    os.remove(previous_instance.image.path)

        except educator_pictures.DoesNotExist:
            pass


