from django.urls import path

from todolist.goals import views


urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view(), name='create_category'),
    path('goal_category/list', views.GoalCategoryListView.as_view(), name='category-list'),
    path('goal_category/<int:pk>', views.GoalCategoryView.as_view(), name='goal-category'),

    path('goal/create', views.GoalCreateView.as_view(), name='create_goal'),
    path('goal/list', views.GoalListView.as_view(), name='goal-list'),
    path('goal/<int:pk>', views.GoalView.as_view(), name='goal'),
]