# Summary 
A minimal URL shortner app with user management made with using **Django**(backend) and **React**(Frontend) and hosted on **Heroku**(at the time of writing).


# Frontend
Front end repo = https://github.com/kakdeykaushik/kinara-frontend



# Live
BASE URL = https://kinara-backend.herokuapp.com/

# Models

## User Model
- username[varchar] - (mandatory field, Unique) users username.
- password[varchar] - (mandatory field) users password.


## Url Model
- short_url[varchar] - (mandatory field) short url.
- original_url[varchar] - (mandatory field) original target url.
- is_active[bool] - status of short_url if it is accessible or not (default = True).
- clicks[int] - number of times url has been accessed (default = 0).
- owner[ForeignKey] - (FK pointing to User model)Owner/creator of the short Url.

# APIs
## 1. User Register = [POST] - "auth/register/"
    - User can enter username and password to create an account(if already not created with given username). It returns a token for Authentication.


## 2. User Login = [POST] - "auth/login/"
    - User can enter username and password to login. It returns a token for Authentication.


## 3. Short URL Create = [POST] - "create/"
    - User can create short url for his/her target url.
    - Authentication required.



## 4. View URL details = [GET] - "details/\<url>/"
    - User can view details of short url like number of times clicked and is active or not.
    - Only owner of short url can view these details.
    - Authentication required.


## 5. Delete URL = [DELETE] - "delete/\<url>/"
    - User can delete the short url.
    - Only owner of short url can perform this action.
    - Authentication required.


## 6. Disable URL = [GET] - "disable/\<url>/"
    - User can disable the short url.
    - Enabled by default.
    - Only owner of short url can perform this action.
    - Authentication required.



## 7. Enable URL = [GET] - "enable/\<url>/"
    - User can enable the short url.
    - Only owner of short url can perform this action.
    - Authentication required.




## 8. Access URL = [GET] - "\<url>/"
    - Anyone with the short url can access this.



# Code Coverage

Code coverage = **85%**


![code-coverage](https://i.imgur.com/r6qQikg.png)

![code-coverage](https://i.imgur.com/sSLUZkA.png)
