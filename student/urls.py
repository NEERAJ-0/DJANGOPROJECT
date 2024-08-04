from django.urls import path
from.import views

urlpatterns = [

    #path('master/',views.master,name='master'),    
    path('home/',views.home,name='home'),    
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),


    #Paths for Insertion
    path('insertbatch/',views.insertbatch,name='insertbatch'),
    path('batch_entry/',views.batch_entry,name='batch_entry'),

    path('insertcourse/',views.insertcourse,name='insertcourse'),
    path('course_entry/',views.course_entry,name='course_entry'),

    path('insertsem/',views.insertsem,name='insertsem'),
    path('sem_entry/',views.sem_entry,name='sem_entry'),

    path('insertexam/',views.insertexam,name='insertexam'),
    path('exam_entry/',views.exam_entry,name='exam_entry'),

    path('insertpaper/',views.insertpaper,name='insertpaper'),
    path('paper_entry/',views.paper_entry,name='paper_entry'),

    path('insertstudent/',views.insertstudent,name='insertstudent'),
    path('student_entry/',views.student_entry,name='student_entry'),

    path('insertstudtrans/',views.insertstudtrans,name='insertstudtrans'),
    path('studtrans_entry/',views.studtrans_entry,name='studtrans_entry'),

    #Paths for Deletion
    path('delete1/<pk>',views.delete1,name='delete1'),
    path('deletecourse/',views.deletecourse,name='deletecourse'),

    path('delete2/<pk>',views.delete2,name='delete2'),
    path('deletebatch/',views.deletebatch,name='deletebatch'),

    path('delete3/<pk>',views.delete3,name='delete3'),
    path('deletesem/',views.deletesem,name='deletesem'),

    path('delete4/<pk>',views.delete4,name='delete4'),
    path('deletepaper/',views.deletepaper,name='deletepaper'),

    path('delete5/<pk>',views.delete5,name='delete5'),
    path('deleteexam/',views.deleteexam,name='deleteexam'),

    path('delete6/<pk>',views.delete6,name='delete6'),
    path('deletestudent/',views.deletestudent,name='deletestudent'),

    path('delete7/<pk>',views.delete7,name='delete7'),
    path('deletestudenttrans/',views.deletestudenttrans,name='deletestudenttrans'),

    #Paths for Updation
    path('update1/<int:course_id>/', views.update1, name='update1'),
    path('updatecourse/',views.updatecourse, name='updatecourse'),

    path('update2/<int:batchno_id>/', views.update2, name='update2'),
    path('updatebatch/',views.updatebatch, name='updatebatch'),

    path('update3/<int:sem_id>/', views.update3, name='update3'),
    path('updatesem/',views.updatesem, name='updatesem'),

    path('update4/<int:papername_id>/', views.update4, name='update4'),
    path('updatepaper/',views.updatepaper, name='updatepaper'),

    path('update5/<int:examtype_id>/', views.update5, name='update5'),
    path('updateexam/',views.updateexam, name='updateexam'),

    path('update6/<int:studname_id>/', views.update6, name='update6'),
    path('updatestudent/',views.updatestudent, name='updatestudent'),

    path('update7/<int:marks_id>/', views.update7, name='update7'),
    path('updatestudenttrans/',views.updatestudenttrans, name='updatestudenttrans'),



    #Paths for Searching
    path('searchbatch/', views.searchbatch, name='searchbatch'),
    path('searchcourse/', views.searchcourse, name='searchcourse'),
    path('searchsem/', views.searchsem, name='searchsem'),
    path('searchpaper/', views.searchpaper, name='searchpaper'),
    path('searchexam/', views.searchexam, name='searchexam'),
    path('searchstudent/', views.searchstudent, name='searchstudent'),
    path('searchstudenttrans/', views.searchstudenttrans, name='searchstudenttrans'),
    
    
    #Paths to display
    path('displaybatch/',views.displaybatch,name='displaybatch'),
    path('displaycourse/',views.displaycourse,name='displaycourse'),
    path('displaysem/',views.displaysem,name='displaysem'),
    path('displayexam/',views.displayexam,name='displayexam'),
    path('displaystudent/',views.displaystudent,name='displaystudent'),
    path('displaypaper/',views.displaypaper,name='displaypaper'),
    path('displaystudenttrans/',views.displaystudenttrans,name='displaystudenttrans'),

    #paths for report
    path('coursereport/',views.coursereport,name='coursereport'),
    path('batchreport/',views.batchreport,name='batchreport'),
    path('semreport/',views.semreport,name='semreport'),
    path('paperreport/',views.paperreport,name='paperreport'),
    path('examreport/',views.examreport,name='examreport'),
    path('studentreport/',views.studentreport,name='studentreport'),
    path('studtransreport/',views.studtransreport,name='studtransreport'),



]