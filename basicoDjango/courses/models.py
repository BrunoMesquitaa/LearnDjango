from django.db import models

class CourseManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | \
            models.Q(descricao__icontains=query))

# Create your models here.
class Course(models.Model):

    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descrição',blank=True)
    startDate = models.DateField('Data de Inicio',null=True,blank=True)
    imagem = models.ImageField(upload_to='cursos/images',verbose_name='Imagem',null=True,blank=True)
    
    create_at = models.DateTimeField('Criado em ',auto_now_add=True)
    update_at = models.DateTimeField('Ultima atualização ',auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ["name"]