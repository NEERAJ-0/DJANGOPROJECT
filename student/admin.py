from django.contrib import admin

from.models import BatchMasterModel
from.models import CourseMasterModel
from.models import SemMasterModel
from.models import ExamMasterModel
from.models import StudentMasterModel
from.models import PaperMasterModel
from.models import StudentInternalTransModel

# Register your models here.

admin.site.register(BatchMasterModel)
admin.site.register(CourseMasterModel)
admin.site.register(SemMasterModel)
admin.site.register(ExamMasterModel)
admin.site.register(StudentMasterModel)
admin.site.register(PaperMasterModel)
admin.site.register(StudentInternalTransModel)