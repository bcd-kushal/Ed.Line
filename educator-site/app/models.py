from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_extension(value):
    allowed_extensions = ['.png', '.jpg', '.jpeg']
    ext = str(value).lower().split('.')[-1]
    if not ext in allowed_extensions:
        raise ValidationError(
            _('Invalid file format. Only PNG and JPG/JPEG are allowed.'),
            code='invalid_image'
        )
    

    


class educator_pictures(models.Model):
    mobile = models.CharField(max_length=11, primary_key=True)
    image = models.ImageField(upload_to='media/static/', validators=[validate_image_extension])
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name