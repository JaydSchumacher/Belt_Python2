# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re


# Create your models here.

class UserManager(models.Manager):
    def creator(self, postData):
        user = self.create(name = postData['name'], alias = postData['alias'], email = postData['email'], password= bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    # def add(self, postData):
    #     newfriend = User.objects.get(id = request.session['curuserid'])
    #     newfriend.friends.add(User.objects.get(id = id))
    #     newfriend = self.add(User.objects.get(id = request.session['curuserid']))
    #     return newfriend

    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        user = self.filter(email = postData['email'])
        
        if len(user) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                results['user'] =  user[0]
            else:
                results['status'] = False
        return results

    def validate(self, postData):
        results = {'status': True, 'errors':[]}

        if len(postData['name']) < 3:
            results['errors'].append('Name too short')
            results['status'] = False
        if postData['name'] ==  '   ':
            results['errors'].append('Name not valid')
            results['status'] = False
        if postData['name'] ==  ' a ':
            results['errors'].append('Name not valid')
            results['status'] = False
        if postData['name'] ==  ' aa':
            results['errors'].append('Name not valid')
            results['status'] = False
        if postData['name'] ==  'a  ':
            results['errors'].append('Name not valid')
            results['status'] = False
        if postData['name'] ==  'aa ':
            results['errors'].append('Name not valid')
            results['status'] = False
        if len(postData['alias']) < 3:
            results['errors'].append('Alias too short')
            results['status'] = False
        if postData['alias'] ==  '   ':
            results['errors'].append('Alias not valid')
            results['status'] = False
        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', postData['email']):
            results['errors'].append('Email not valid')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append('Passwords does not match')
            results['status'] = False
        if len(postData['password']) < 5:
            results['errors'].append('Passwords must be at least 5 characters')
            results['status'] = False
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False
        
        return results
        

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    friends = models.ManyToManyField('self')
    objects = UserManager()
