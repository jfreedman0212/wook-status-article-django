from django.contrib import admin
from . import models

admin.site.register(models.Project, models.ProjectAdmin)
admin.site.register(models.Nominator, models.NominatorAdmin)
admin.site.register(models.Continuity)
admin.site.register(models.Nomination, models.NominationAdmin)

