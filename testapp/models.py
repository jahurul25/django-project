from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=50, unique=True)
    slug      = models.SlugField(unique=True)
    creatAt   = models.DateTimeField(auto_now_add=True)
    updateAt  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dept_name

    def get_absolute_url(self):
        return reverse('department', kwargs={'slug': self.slug})    
 
        
def pre_save_dept_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.dept_name)
    exists = Department.objects.filter(slug = slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug    

pre_save.connect(pre_save_dept_post_receiver, sender=Department)    