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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# APIs imports
from serapide_core import urls as serapide_code_urls
# Wagatail imports
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls


# Dajngo admin
urlpatterns = [
    path('django-admin/', admin.site.urls),
]

# Apps urls
urlpatterns += [
    path('', include('strt_portal.urls')),
    path('users/', include('strt_users.urls'))
]

# APIs urls
urlpatterns += [
    path('', include(serapide_code_urls)),
]

# Wagtail urls
urlpatterns += [
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
