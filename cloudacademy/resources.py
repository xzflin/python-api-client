#!/usr/bin/env python
#
# Copyright (c) 2014, Cloud Academy, Inc.
# Author: Giacomo Marinangeli <giacomo@cloudacademy.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of cloudacademy nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json, requests
from .exceptions import ResourceException

class BaseResource(object):
    path = None
    methods = []
    
    def __init__(self,connection):
        assert self.path
        super(BaseResource, self).__init__()
        self.connection = connection
    
    def __getattr__(self, method):
        try:
            callback = super(BaseResource,self).__getattribute__("method_%s" % method)
        except AttributeError:
            raise ResourceException("%s invalid method" % method)
        if method in self.methods:
            return callback
        else:
            raise ResourceException("Method %s not implemented for this resource" % method)
    
    def _make_url(self,**kwargs):
        try:
            return "%s%s" % (self.connection.baseurl,self.path % kwargs)
        except KeyError, e:
            raise ResourceException("Missing resource params: %s" % ", ".join(e.args))
            
    def _make_request(self,method,**kwargs):
        url = self._make_url(**kwargs)
        params = {"url":url,"auth":self.connection.auth}
        if method == "post":
            params.update({"data":json.dumps(kwargs),"headers":{'Content-Type': 'application/json'}})
        response = getattr(requests,method)(**params)
        return response.json()
            
    def method_get(self,**kwargs):
        return self._make_request("get",**kwargs)

    def method_post(self,**kwargs):
        return self._make_request("post",**kwargs)
        
    def method_put(self,**kwargs):
        return self._make_request("put",**kwargs)  
        
    def method_delete(self,**kwargs):
        return self._make_request("delete",**kwargs)        
    
class LeaderBoard(BaseResource):
    path = "/leaderboard/"
    methods = ["get"]
    
class UserList(BaseResource):
    path = "/users/"
    methods = ["get","post"]

class UserCloudRank(BaseResource):
    path = "/users/%(user_id)s/cloudrank/"
    methods = ["get"]
        
class User(BaseResource):
    path = "/users/%(user_id)s/"
    methods = ["get","put","delete"]
        
class Quiz(BaseResource):
    path = "/quiz/%(provider_id)s/"
    methods = ["get"]
    
class QuizByTag(BaseResource):
    path = "/quiz/%(provider_id)s/%(tag_id)s/"
    methods = ["get"]    
    
class QuizAnswer(BaseResource):
    path = "/quiz/simple/%(quiz_id)s/"
    methods = ["get","post"]    
    
class CourseListResource(BaseResource):
    path = "/courses/"
    methods = ["get","post"]    
    
class CourseResource(BaseResource):
    path = "/courses/%(course_id)s/"
    methods = ["get","post"]    
