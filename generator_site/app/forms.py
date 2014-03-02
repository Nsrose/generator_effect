from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class submission_form(Form):
    submission = TextField('submission', validators = [Required()])
    