# PollWorldBackend
Server-side django application for PollWorld project

Endpoints:
  - /accounts/api/register/ - register user
  - /token/ - login user
  - /accounts/api/get/ (GET) - get currently logged user
  - /accounts/api/update/ (PUT) - update user personal data
  - /accounts/api/change-pass/ - change user password (TBA)
  - /api/login/social/jwt-pair/ - login with facebook
  - /polls/all/ (GET) - get polls for current user
  - /polls/{id}/ (GET) - get poll with id
