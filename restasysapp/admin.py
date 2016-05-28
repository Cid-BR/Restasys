from django.contrib import admin
from .models import Mesa, Pratos, Pedidos, Pedidos_Fechados

admin.site.register(Mesa)
admin.site.register(Pratos)
admin.site.register(Pedidos)
admin.site.register(Pedidos_Fechados)
