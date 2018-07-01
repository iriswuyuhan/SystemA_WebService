
$('#login').click(
    function () {
        let s_id = $('#username').val();
        let password = $('#password').val();

        $.ajax({
            type: 'GET',
            url: '/usrlogin',
            data: {
                account: s_id,
                password: password
            },
            success: function (result) {
                if (result) {
                    $('#loginAndSign').hide();
                    document.getElementById("user").innerText = s_id;
                    $('#welcomeUser').show();
                    localStorage.setItem('account', s_id);
                } else {
                    alert("登录失败");
                }
            },
            error: function (xhr) {
                console.log(xhr);
            }

        })
    }
);

$('#managerLogin').click(function () {
    let manager =  $('#managerName').val();
    let password = $('#managePass').val();

    $.ajax({
        type: 'GET',
        url: '/adminlogin/',
        data: {
            account: manager,
            password: password
        },
        success: function (result) {
            if (result) {
                localStorage.setItem('account', manager);
                window.location.href = "../manager";
            } else {
                alert("登录失败");
            }
        },
        error: function (xhr) {
            console.log(xhr);
        }

    })
});

function check() {
    if (localStorage.getItem('account') === null) {
        window.location.href = 'index.html';
    } else {
        document.getElementById('user').innerText = localStorage.getItem('account');
    }
}