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

from cloudacademy import CloudAcademy

aws = "5242fc36af1762274b68951f"
access="YjlhZWFkMDEwNmM3ZDZiZjFkMzk5ODI3MmY2M2Q5ZTEyZGNmODZmNA"
secret="MDM3YTZjYzFhNzdhNDA1MmFhZjVjMDgzNWE0NWMxOTFhM2Q0ZjU2Mw"
    
ca = CloudAcademy(access,secret)

exit=False
while not exit:
    quiz = ca.quiz.get(provider_id=aws)
    print quiz['description']
    for answer in quiz['answers']:
        print " [%(id)s] %(description)s" % answer
    print
    
    user_answer = None
    while not user_answer:
        try:
            user_answer = int(raw_input("Your answer: "))
        except KeyboardInterrupt:
            exit=True
            break
        except:
            user_answer = None
            
        if user_answer not in [a['id'] for a in quiz['answers']]:
            user_answer = None
            
    if not exit:
        result = ca.quiz_answer.post(quiz_id=quiz['_id'],action="answer",answer_id=user_answer)
        print result['msg']
        print

