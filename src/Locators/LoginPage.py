class LoginPage:
    class CreateCustomer:
        title = {'CSS_SELECTOR': "select[id='register.title']"}
        first_name = {'CSS_SELECTOR': "input[id='register.firstName']"}
        last_name = {'CSS_SELECTOR': "input[id='register.lastName']"}
        email = {'CSS_SELECTOR': "input[id='register.email']"}
        password = {'CSS_SELECTOR': "#password"}
        confirm_password = {'CSS_SELECTOR': "input[id='register.checkPwd']"}
        consent_checkbox = {'CSS_SELECTOR': "input[id='consentForm.consentGiven1']"}
        terms_checkbox = {'CSS_SELECTOR': "#registerChkTermsConditions"}
        register_button = {'CSS_SELECTOR': ".btn.btn-default.btn-block"}

    class Login:
        email = {'CSS_SELECTOR': "#j_username"}
        password = {'CSS_SELECTOR': "#j_password"}
        login_button = {'CSS_SELECTOR': "button[class='btn btn-primary btn-block']"}

