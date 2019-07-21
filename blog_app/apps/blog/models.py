from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogManager(models.Manager):
    pass

class Blog(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

    def __unicode__(self):
        return "Blog ID: " + str(self.id) + ", Blog Name: " + self.name + ", Blog Description: " + self.desc

class CommentManager(models.Manager):
    pass


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    blog = models.ForeignKey(Blog, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __unicode__(self):
        return "Comment ID: " + str(self.id) + ", Blog: " + self.blog

class AdminManager(models.Manager):
    pass

class Admin(models.Model):
    name = models.CharField(max_length=100)
    blogs = models.ManyToManyField(Blog, related_name="admins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdminManager()

    def __unicode__(self):
        return "Admin ID: " + str(self.id) + ", Admin Name: " + self.name + ", Admin Blogs: " + self.blogs
