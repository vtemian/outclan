
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns("chat.views",
    url("^$", "rooms", name="rooms"),
    url("^create/$", "create", name="create"),
    url("^(?P<slug>.*)$", "room", name="room"),
)
