from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import SafeData, SafeString, mark_safe


# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.name

class Thana(models.Model):
    district=models.ForeignKey(District, related_name='district', related_query_name='tag', on_delete=models.CASCADE)
    name=models.CharField(max_length=25, blank=False)
    
    def __str__(self):
        return self.name
        #return 'District:' + self.district.name +', Thana:'+ self.name

class Department(models.Model):
    name=models.CharField(max_length=100, blank=False, unique=True)
    
    def __str__(self):
        return self.name

class Designation(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name

class EmpBasicInfo(models.Model):
    emp_status=(
        ('Permanent','Permanent'),
        ('Trainee','Trainee'),
    )
    emp_id=models.CharField(max_length=15, unique=True, blank=False, null=True, db_column='emp_id', db_index=True)
    first_name=models.CharField(max_length=50, help_text="""<b>Employee First Name</b>""")
    last_name=models.CharField(max_length=50, blank=True)
    dob=models.DateField()
    image = models.ImageField(upload_to='emp_images', null=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15, unique=True)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    thana=models.ForeignKey(Thana, on_delete=models.CASCADE)
    joiningdate=models.DateField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    designation=models.ForeignKey(Designation, on_delete=models.CASCADE)
    status=models.CharField(max_length=15, choices=emp_status)
    remarks=models.TextField()

    def __str__(self):
        return self.first_name +' '+ self.last_name

    def dob_tag(self):
        return self.dob
    dob_tag.short_description = 'Birth Date'
    dob_tag.allow_tags = True

    def joiningdate_tag(self):
        return self.joiningdate
    joiningdate_tag.short_description = 'Joining Date'
    joiningdate_tag.allow_tags = True

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
class EmpSalary(models.Model):
    employee=models.ForeignKey(EmpBasicInfo, on_delete=models.CASCADE)
    basicsalary=models.FloatField()
    medical=models.FloatField()
    houserent=models.FloatField()
    others=models.FloatField()

    def __str__(self):
        return str(self.basicsalary + self.medical + self.houserent + self.others)
    
    
class EmpEducation(models.Model):
    exam=(
        ('SSC','SSC'),
        ('HSC','HSC'),
        ('Bachelor','Bachelor'),
    )
    employee=models.ForeignKey(EmpBasicInfo, on_delete=models.CASCADE)
    degree=models.CharField(max_length=10, choices=exam)
    institute=models.CharField(max_length=100)
    passingyear=models.IntegerField()
    result=models.CharField(max_length=5)

    def __str__(self):
        return self.employee.first_name + ' ' + self.degree

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

class Card(models.Model):

    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit.choices, verbose_name='Suit')

    def __str__(self):
        return str(self.suit)
    

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog1', related_query_name='tag', on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


