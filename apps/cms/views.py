# cmd/views.py
__author__ = 'derek'

from flask import Blueprint,views,render_template,request,session
from flask import url_for,redirect
from .forms import LoginForm
from .models import CMSUser

bp = Blueprint("cms",__name__,url_prefix='/cms')

@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

def index():
    return 'cms index'

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                if remember:
                    # 31天后过期
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='用户名或密码错误')

        else:
            #form.errors的错误信息格式，是一个字典，value是列表的形式
            # {'email': ['请输入正确的邮箱格式'], 'password': ['密码长度不够或超出']}
            message = form.errors.popitem()[1][0]
            return self.get(message=message)

bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))

@bp.route('/logout')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return jsonify({"code":200,"message":""})
            else:
                return jsonify({"code":400,"message":"旧密码错误"})
        else:
            message = form.get.error()
            return jsonify({"code":400,"message":message})


bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'),strict_slashes=False)