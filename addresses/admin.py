from django.contrib import admin

from addresses.models import Location, Datacenter, Network, Addresses

admin.site.register(Location)
admin.site.register(Datacenter)
admin.site.register(Network)
admin.site.register(Addresses)
