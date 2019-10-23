window.fbAsyncInit = function () {
    FB.init({
        appId: '2115478052091458',
        cookie: true,
        xfbml: true,
        version: 'v4.0'
    });
};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) { return; }
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function facebookLogin() {
    FB.login(function (response) {
        console.log(response.authResponse.userID);
    }, { scope: 'public_profile,user_posts' })
}

function getUserData() {
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name', 'GET', function (response) {
                console.log(response);
            });
        }
    });
}

function facebookLogout() {
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.logout();
        }
    });
}
