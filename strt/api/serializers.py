# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################

from rest_framework import serializers
from strt_users.models import MembershipType


class MembershipTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipType
        fields = '__all__'
