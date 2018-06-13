/**
 * Created by Administrator on 2018/6/3.
 */


$(function () {
    $("#submit").click(function (event) {
        //阻止按钮的提交表单的事件
        event.preventDefault();
        //分别获取三个标签
        var oldpwdE = $("input[name=oldpwd]");
        var newpwdE = $("input[name=newpwd]");
        var newpwd2E = $("input[name=newpwd2]");

        var oldpwd = oldpwdE.val();
        var newpwd = newpwdE.val();
        var newpwd2 = newpwd2E.val();

        //1.要在模板的meta标签中渲染一个csrf-token
        //2.在ajax请求的头部汇总设置X-CSRFtoken
        zlajax.post({
            'url':'/cms/resetpwd',
            'data':{
                'oldpwd':oldpwd,
                'newpwd':newpwd,
                'newpwd2':newpwd2
            },
            'success':function (data) {
                console.log(data);
            },
            'fail':function (error) {
                console.log(error);
            }
        });
    });
});