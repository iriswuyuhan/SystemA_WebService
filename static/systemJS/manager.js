$().ready(function () {
    // check();
    $('#all').click();
});

$('#add').click(function () {
    $('#course_table').hide();
    $('#course_info').show();

    $('#add').addClass("active-menu");
    $('#all').removeClass("active-menu");
    $('#view').text("添加课程");

});

$('#all').click(function () {
    $('#course_table').show();
    $('#course_info').hide();

    $('#all').addClass("active-menu");
    $('#add').removeClass("active-menu");
    $('#view').text("全部课程");
    loadAllCourse();
});

$('#addCourse').click(function () {
    addCourse();
});

//管理员添加课程
function addCourse() {
    let course = {};
    course.cnm = $('#name').val();
    course.credit = $('#credit').val();
    course.teacher = $('#teacher').val();
    course.room = $('#location').val();
    course.share = $('input[name="share"]:checked').val();

    
    $.ajax({
        type: 'POST',
        url: '/course/add/',
        contentType: 'application/json',
        data: JSON.stringify(course),
        success: function (result) {
            console.log(result);
            if (result) {
                alert("添加成功！");
                window.location.reload();
            } else {
                alert("添加失败！请查看信息填写是否有错");
            }

        },
        error: function (xhr) {
            console.log(xhr.status);
            console.log(xhr.error);
        }
    })
}


function loadAllCourse() {
    $.ajax({
        type: 'GET',
        url: '/course/getAll',
        data: {},
        dataType: 'text',
        success: function (result) {
            let resultList = parseXML(result).getElementsByTagName("a:课程");
            for (let i = 0; i < resultList.length; i++) {
                let share = "";
                let color = "lightskyblue";
                if (resultList[i].getElementsByTagName("a:共享")[0].firstChild.nodeValue === "Y") {
                    share = "已共享";
                } else {
                    share = "未共享";
                    color = "gray";
                }
                $('#course_table').append(
                    '<tr>' +
                    '<td>' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("a:课程名称")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("a:学分")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("a:授课老师")[0].firstChild.nodeValue + '</td>' +
                    '<td>' + resultList[i].getElementsByTagName("a:授课地点")[0].firstChild.nodeValue + '</td>' +
                    '<td><label style="color: '+ color +'">'+ share +'</label></td>' +
                    '<td>' +
                    '<button class="btn btn-link" id="delete_' + i + '">删除</button>' +
                    '</td>' +
                    '</tr>' +
                    '<script>' +
                    '$("#delete_' + i + '").click(function() {' +
                    'deleteCourse("' + resultList[i].getElementsByTagName("a:课程编号")[0].firstChild.nodeValue + '")' +
                    '});' +
                    '</script>'
                );
            }


        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
        }

    })
}

//管理员删除课程
function deleteCourse(cno) {
    $.ajax({
        type: 'GET',
        url: '/course/remove',
        data: {
            cid: cno
        },
        success: function (result) {
            if (result) {
                location.reload();
            } else {
                alert("请勿重复删除！");
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest.status);
            console.log(XMLHttpRequest.readyState);
        }
    })
}