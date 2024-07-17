from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.NominatorRight)
admin.site.register(models.Nominator)
admin.site.register(models.NominatorRightTimeframe)
admin.site.register(models.Continuity)
admin.site.register(models.Nomination, models.NominationAdmin)

