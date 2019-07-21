from __future__ import unicode_literals

from django.db import models 
from PIL import Image

import md5
import bcrypt
import os, binascii

import re
NAME_REGEX =re.compile('^[A-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, postData):
        messages = []
        email = postData['email']
        password = postData['password']
        if len(str(email)) < 1:
            messages.append("email must not be blank!")
        if len(str(email)) < 2:
            messages.append("email must be at least 2 characters long!")
        if len(str(password)) < 1:
            messages.append("password must not be blank")
        if len(str(password)) < 8:
            messages.append("password must be at least 8 characters long!")
        if User.objects.filter(email=email):
            # encode the password to a specific format since the above email is registered
            login_pw = password.encode()
            # encode the registered user's password from database to a specific format
            db_pw = User.objects.get(email=email).password.encode()
            # compare the password with the password in database
            if not bcrypt.checkpw(login_pw, db_pw):
                messages.append("Password is Incorrect!")
        else:
            messages.append("Email has already been registered!")
        return messages

    def register(self, postData):
            print "register process"
            messages = []
            firstName = postData['firstName']
            if len(str(firstName)) < 1:
                messages.append("Error! First name must not be blank!")
            if len(str(firstName)) < 2:
                messages.append("Error! First name must be at least 2 characters long!")

            lastName = postData['lastName']
            if len(str(lastName)) < 1:
                messages.append("Error! Last name must not be blank!")
            if len(str(lastName)) < 2:
                messages.append("Error! Last name must be at least 2 characters long!")

            email = postData['email']
            if len(str(email)) < 1:
                messages.append("Error! Email must not be blank!")
            if len(str(email)) < 2:
                messages.append("Error! Email must be at least 2 characters long!")
            if not EMAIL_REGEX.match(email):
                messages.append("Error! Email must be in a valid format!")

            password = postData['password']
            if len(str(password)) < 1 :
                messages.append("Error! Password must not be blank!")
            if len(str(password)) < 8 :
                messages.append("Error! Password must be at least 8 characters long!")

            pwConfirm = postData['pwConfirm']
            if pwConfirm != password:
                messages.append("Error! Passwords must match")
            user_list = User.objects.filter(email=email)
            for user in user_list:
                print user.email
            if user_list:
                messages.append("Error! Email is already in the system!")
            if not messages:
                print "No messages"
                password = password.encode()
                salt = bcrypt.gensalt()
                hashed_pw = bcrypt.hashpw(password, salt)
                # password = password
                print "Create User"
                print hashed_pw
                User.objects.create(firstName=firstName, lastName=lastName, email=email, password=hashed_pw)
                print hashed_pw
                print User.objects.all()
                return None
            return messages

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=25)
    pwConfirm = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
# Create your models here.

    def __unicode__(self):
        return "id: " + str(self.id) + ", firstName: " + str(self.firstName) + ", Last Name: " + str(self.lastName) + ", Username: " + str(self.userName) + ", Email: " + str(self.email)+ ", Password:" + str(self.password) + ", Password Confirmation:" + str(self.pwConfirm)

class ProjectManager(models.Manager):
    def createproject(self, postData):
        messages = []

        # founder = name
        # print "{} is the founder of this motherfucking project!".format(founder)

        title = postData['title']
        if len(str(title)) < 1:
            messages.append("Error! Title must not be blank!")
        if len(str(title)) < 10:
            messages.append("Error! Title must be at least 10 characters long!")
        
        about = postData['about']
        if len(str(about)) < 1:
            messages.append("Error! About section must not be blank!")
        if len(str(about)) < 20:
            messages.append("Error! About section must be at least 20 characters long!")

        goal = postData['goal']
        if goal < 1:
            messages.append("Error! Goal must be at least $10!")

        # I deleted progress field on form - It should just be ZERO
        # progress = postData['progress']
        # print "{} is the progress".format(progress)

        if not messages:
            print "Success! No Errors!"
            Project.objects.create(title=title, about=about, goal=goal, progress=0, percentage=0, picture=postData['picture'])
            #Removed Founder - FOR NOW
            return None
        return messages

    def donate(self, postData):
        messages = []
        current_project = Project.objects.all()
        # current_project = Project.object.get(id=id)
        #Added ID Parameter and it didn't work
        # print "Current Project: {}".format(current_project)
        donation = postData['donation']
        print donation
        # current_project.progress = current_project.progress
        if donation < 1:
            messages.append("Please Make A Donation Of At Least $5!")
        if not messages:
            current_project.update(progress=donation)
            return donation
        return messages

class Project(models.Model):
    title = models.CharField(max_length=55)
    #Potentially add ProjectFounder Field (equal to request.session['name'])
    founder = models.ForeignKey(User, related_name="founder", null=True, blank=True)
    about = models.CharField(max_length=1000)
    goal = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    percentage = models.FloatField(null=True, blank=True)
    donations = models.ForeignKey(User, related_name="donors", blank=True,
    null=True)
    picture = models.ImageField(upload_to="project_image", blank=True)
    # Above Line just added as a trial
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", Project Title: " + str(self.title) + ", About Project: " + str(self.about) + ", Goal: $" + str(self.goal) + ", Progress: $" + str(self.progress)+ ", Percentage:" + str(self.percentage) + ", Donations:" + str(self.donations)
