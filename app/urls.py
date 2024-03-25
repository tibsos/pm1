from django.urls import path, include

from .views import *

app_name = 'app'

urlpatterns = []

tasks_urlpatterns = [

    path('tasks', tasks, name = 'tasks'),
    path('create-task', create_task, name = 'create-task'),
    path('complete-task', complete_task, name = 'complete-task'),

]

folder_urlpatterns = [

    path('create-folder/', create_folder, name = 'create-folder'),
    path('get-folder/<uuid:uid>/', get_folder, name = 'get-folder'),
    path('edit-folder/', edit_folder, name = 'edit-folder'),
    path('delete-folder/', delete_folder, name = 'delete-folder'),

    path('add-folder/', add_folder, name = 'add-folder'),
    path('remove-folder/', remove_folder, name = 'remove-folder'),

]

notes_urlpatterns = [

    path('home', app, name = 'app'),
    path('dom/', home, name = 'home'),

    path('loved/', loved, name = 'loved'),
    path('archive/', archive, name = 'archive'),

    path('trash/', trash, name = 'trash'),
    path('empty-trash', empty_trash, name = 'empty-trash'),

    path('search/', search_notes, name = 'search'),
    path('cancel-search/', cancel_search, name = 'cancel-search'),

]

note_urlpatterns = [

    path('create-note/', create_note, name = 'create-note'),
    path('get-note/<uuid:uid>/', get_note, name = 'get-note'),

    path('love-note/', love_note, name = 'love-note'),
    path('pin-note/', pin_note, name = 'pin-note'),
    path('archive-note/', archive_note, name = 'archive-note'),
    path('delete-note/', delete_note, name = 'delete-note'),

    path('update-contents/', update_contents, name = 'update-contents'),
    path('update-title/', update_title, name = 'update-title'),
    path('update-content/', update_content, name = 'update-content'),

    path('delete-photo/', delete_photo, name = 'delete-photo'),
    path('upload-photo-to-note/',  upload_photo_to_note, name = 'upload-photo-to-note'),

]

payment_urlpatterns = [

    path('initiate-payment/', initiate_payment, name = 'initiate-payment'),
    path('payment-notifications', payment_notifications, name = 'payment-notifications'),
    path('check-subscription-expiration/', check_subscription_expiration, name = 'check-subscription-expiration'),

]

mobile_urlpatterns = [

    path('create-first-note', create_first_note, name = 'create-first-note'),

    path('create-note-mobile', create_note_mobile, name = 'create-note-mobile'),

]

urlpatterns += folder_urlpatterns
urlpatterns += notes_urlpatterns
urlpatterns += note_urlpatterns
urlpatterns += tasks_urlpatterns
urlpatterns += payment_urlpatterns
urlpatterns += mobile_urlpatterns