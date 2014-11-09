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

from .resources import User, UserList, LeaderBoard, UserCloudRank,RandomQuiz,SimpleQuiz
from .exceptions import ResourceException

class CloudAcademy(object):
    """docstring for CloudAcademy"""
    
    #_baseurl = "https://cloudacademy.com/api/v%d"
    _baseurl = "http://local.cloudacademy.com:5000/api/v%d"
    
    resources = {
        'leaderboard':      LeaderBoard,
        'user':             User,
        'user_cloudrank':   UserCloudRank,
        'user_list':        UserList,
        'quiz_random':      RandomQuiz,
        'quiz_simple':      SimpleQuiz,
    }
    
    def __init__(self, access, secret,version=1):
        super(CloudAcademy, self).__init__()
        self.auth = (access,secret)
        self.version = version
        self.baseurl = self._baseurl % version
        
    def __getattr__(self, attribute_name):
        try:
            return self.resources[attribute_name](self)
        except KeyError:
            #return super(CloudAcademy, self).__getattribute__(attribute_name)
            raise ResourceException("%s is not a valid resource" % attribute_name)
            
            
    
    